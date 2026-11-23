#!/usr/bin/env python3
"""Fail closed when private or unsafe material appears in the public repo."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


REQUIRED_PATHS = (
    ".gitignore",
    "README.md",
    "PROTOCOL.md",
    "DISCLAIMER.md",
    "PRIVACY.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "LICENSE-DOCS.md",
    "TRADEMARK.md",
    "schemas/evidence.schema.json",
    "schemas/fact.schema.json",
    "schemas/source.schema.json",
    "schemas/approval.schema.json",
    "docs/agent-architecture.md",
    "docs/legal-source-pipeline.md",
    "docs/codex-chrome-source-capture.md",
    "docs/evidence-collection-playbook.md",
    "docs/founder-story.md",
    "docs/project-journey.md",
    "docs/protocols/README.md",
    "docs/protocols/anti-hallucination-protocol.md",
    "docs/protocols/truth-five-protocol.md",
    "docs/protocols/aep-adoption.md",
    "docs/protocols/agent-configuration.md",
    "examples/agent-config/README.md",
    "examples/agent-config/AGENTS.template.md",
    "examples/agent-config/project.example.yaml",
    "examples/agent-config/roles.example.yaml",
    "examples/agent-config/role-contract.template.md",
    "examples/agent-config/STATUS.template.md",
    "examples/agent-config/decisions.template.md",
    "examples/agent-config/worklog.template.md",
    "examples/legal-sources/source-register.template.md",
    "examples/legal-sources/download-run.template.md",
    "examples/legal-sources/rule-use-matrix.template.md",
    "examples/evidence/README.md",
    "examples/evidence/collection-plan.template.md",
    "examples/evidence/collection-run.template.md",
    "examples/evidence/legal-evidence-matrix.template.md",
    "skills/legal-source-archive/SKILL.md",
    "examples/synthetic/case.json",
    "examples/synthetic/LICENSE-CC0.md",
    "tools/check_public_safety.py",
    "tests/test_check_public_safety.py",
    "tests/test_founder_story.py",
    "tests/test_agent_architecture.py",
    "tests/test_legal_source_pipeline.py",
    "tests/test_evidence_collection_playbook.py",
)

SKIPPED_DIR_NAMES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}

BLOCKED_SUFFIXES = {
    ".7z",
    ".avi",
    ".bmp",
    ".csv",
    ".db",
    ".dmg",
    ".doc",
    ".docx",
    ".eml",
    ".flac",
    ".gif",
    ".gz",
    ".heic",
    ".jpeg",
    ".jpg",
    ".key",
    ".m4a",
    ".m4v",
    ".mkv",
    ".mov",
    ".mp3",
    ".mp4",
    ".msg",
    ".p12",
    ".pdf",
    ".pem",
    ".pfx",
    ".png",
    ".ppt",
    ".pptx",
    ".rar",
    ".sqlite",
    ".sqlite3",
    ".tar",
    ".tif",
    ".tiff",
    ".tsv",
    ".wav",
    ".webp",
    ".xls",
    ".xlsx",
    ".zip",
}

BLOCKED_NAMES = {
    ".env",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "credentials",
    "credentials.json",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "id_rsa",
    "secrets.json",
}

SENSITIVE_PATTERNS: tuple[tuple[str, re.Pattern[str], str], ...] = (
    (
        "possible mainland China identity number",
        re.compile(
            r"(?<!\d)[1-9]\d{5}"
            r"(?:18|19|20)\d{2}"
            r"(?:0[1-9]|1[0-2])"
            r"(?:0[1-9]|[12]\d|3[01])"
            r"\d{3}[\dXx](?!\d)"
        ),
        "Replace identity numbers with a clearly fictional token.",
    ),
    (
        "possible mainland China mobile number",
        re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
        "Do not commit phone numbers; use a fictional placeholder.",
    ),
    (
        "possible court case number",
        re.compile(
            r"\(\s*(?:19|20)\d{2}\s*\)\s*"
            r"[\u4e00-\u9fff]{1,8}\d{2,8}"
            r"[\u4e00-\u9fff]+\d{1,8}号"
        ),
        "Real or case-specific court numbers belong in the private workspace.",
    ),
    (
        "possible long order or transaction number",
        re.compile(r"(?<!\d)\d{16,25}(?!\d)"),
        "Mask long order, payment, account, or transaction identifiers.",
    ),
    (
        "possible OpenAI-style secret",
        re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}"),
        "Revoke the credential and remove it from Git history.",
    ),
    (
        "possible GitHub token",
        re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{20,}"),
        "Revoke the credential and remove it from Git history.",
    ),
    (
        "possible AWS access key",
        re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])"),
        "Revoke the credential and remove it from Git history.",
    ),
    (
        "private key material",
        re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
        "Private keys must never enter the public repository.",
    ),
    (
        "blocked public platform name",
        re.compile("\u98de\u732a|\u6dd8\u5b9d"),
        "Use the repository aliases F猪 and T宝 instead.",
    ),
)


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    kind: str
    message: str
    evidence: str = ""


@dataclass(frozen=True)
class ScanResult:
    findings: tuple[Finding, ...]
    files_scanned: int

    @property
    def ok(self) -> bool:
        return not self.findings


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _iter_repository_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file() and not path.is_symlink():
            continue
        relative_parts = path.relative_to(root).parts
        if any(part in SKIPPED_DIR_NAMES for part in relative_parts):
            continue
        yield path


def _redact(value: str) -> str:
    if len(value) <= 4:
        return "*" * len(value)
    return f"{value[:2]}{'*' * min(len(value) - 4, 16)}{value[-2:]}"


def _check_name(path: Path, root: Path) -> Finding | None:
    name = path.name.lower()
    if name in BLOCKED_NAMES or name.startswith(".env."):
        return Finding(
            _relative(path, root),
            0,
            "blocked-name",
            "Environment and credential files are not allowed.",
        )
    if path.suffix.lower() in BLOCKED_SUFFIXES:
        return Finding(
            _relative(path, root),
            0,
            "blocked-file-type",
            f"Attachment or generated media type is not allowed: {path.suffix.lower()}",
        )
    return None


def _decode_text(path: Path, root: Path) -> tuple[str | None, Finding | None]:
    raw = path.read_bytes()
    if b"\x00" in raw:
        return None, Finding(
            _relative(path, root),
            0,
            "binary-file",
            "Binary files are not allowed in this text-only public repository.",
        )
    try:
        return raw.decode("utf-8-sig"), None
    except UnicodeDecodeError:
        return None, Finding(
            _relative(path, root),
            0,
            "non-utf8-file",
            "Only UTF-8 text files are allowed.",
        )


def check_repository(root: str | Path) -> ScanResult:
    """Return all public-safety findings for a repository directory."""

    root_path = Path(root).resolve()
    if not root_path.is_dir():
        return ScanResult(
            (
                Finding(
                    ".",
                    0,
                    "missing-root",
                    f"Repository directory does not exist: {root_path}",
                ),
            ),
            0,
        )

    findings: list[Finding] = []
    for required in REQUIRED_PATHS:
        if not (root_path / required).is_file():
            findings.append(
                Finding(
                    required,
                    0,
                    "missing-required-file",
                    "Required public repository file is missing.",
                )
            )

    files_scanned = 0
    for path in _iter_repository_files(root_path):
        relative = _relative(path, root_path)
        name_finding = _check_name(path, root_path)
        if name_finding:
            findings.append(name_finding)
            continue
        if path.is_symlink():
            findings.append(
                Finding(
                    relative,
                    0,
                    "symlink",
                    "Symlinks are not allowed; they can point outside the public tree.",
                )
            )
            continue

        text, decode_finding = _decode_text(path, root_path)
        if decode_finding:
            findings.append(decode_finding)
            continue
        if text is None:
            continue

        files_scanned += 1
        if path.suffix.lower() == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                findings.append(
                    Finding(
                        relative,
                        exc.lineno,
                        "invalid-json",
                        f"Invalid JSON: {exc.msg}.",
                    )
                )

        for line_number, line in enumerate(text.splitlines(), start=1):
            for kind, pattern, remedy in SENSITIVE_PATTERNS:
                for match in pattern.finditer(line):
                    findings.append(
                        Finding(
                            relative,
                            line_number,
                            kind,
                            remedy,
                            _redact(match.group(0)),
                        )
                    )

    return ScanResult(tuple(sorted(findings)), files_scanned)


def _format_finding(finding: Finding) -> str:
    location = finding.path
    if finding.line:
        location = f"{location}:{finding.line}"
    message = f"ERROR {location}: {finding.kind}: {finding.message}"
    if finding.evidence:
        message = f"{message} Evidence: {finding.evidence}"
    return message


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check that the public repository contains only safe text material."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root to scan. Defaults to the current directory.",
    )
    args = parser.parse_args(argv)

    result = check_repository(args.root)
    if not result.ok:
        for finding in result.findings:
            print(_format_finding(finding), file=sys.stderr)
        print(
            f"FAIL: {len(result.findings)} public-safety finding(s); "
            f"{result.files_scanned} file(s) scanned.",
            file=sys.stderr,
        )
        return 1

    print(f"PASS: public-safety checks passed ({result.files_scanned} files scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
