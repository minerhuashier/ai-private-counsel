from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.check_public_safety import REQUIRED_PATHS, check_repository


class PublicSafetyCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self._write_clean_repository()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _write(self, relative: str, content: str | bytes = "") -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")

    def _write_clean_repository(self) -> None:
        for relative in REQUIRED_PATHS:
            if relative.endswith(".json"):
                content = "{}\n"
            elif relative == ".gitignore":
                content = "private/\n.env\n"
            else:
                content = f"# Safe placeholder for {relative}\n"
            self._write(relative, content)

    def _kinds(self) -> set[str]:
        return {finding.kind for finding in check_repository(self.root).findings}

    def test_clean_repository_passes(self) -> None:
        result = check_repository(self.root)

        self.assertTrue(result.ok, result.findings)
        self.assertGreater(result.files_scanned, 0)

    def test_blocked_attachment_is_rejected(self) -> None:
        self._write("notes/court-document.pdf", b"%PDF-fictional-test")

        self.assertIn("blocked-file-type", self._kinds())

    def test_mobile_number_is_rejected_without_echoing_full_value(self) -> None:
        value = "138" + "0013" + "8000"
        self._write("notes/contact.md", f"Call {value}\n")

        result = check_repository(self.root)
        matches = [
            item
            for item in result.findings
            if item.kind == "possible mainland China mobile number"
        ]

        self.assertEqual(1, len(matches))
        self.assertNotIn(value, matches[0].evidence)

    def test_identity_number_is_rejected(self) -> None:
        value = "110105" + "19491231" + "002X"
        self._write("notes/profile.md", f"ID: {value}\n")

        self.assertIn(
            "possible mainland China identity number",
            self._kinds(),
        )

    def test_public_platform_names_are_rejected(self) -> None:
        for value in ("\u98de\u732a", "\u6dd8\u5b9d"):
            with self.subTest(value=value):
                self._write("notes/platform.md", f"{value}\n")

                self.assertIn("blocked public platform name", self._kinds())

    def test_missing_required_file_is_rejected(self) -> None:
        (self.root / "PRIVACY.md").unlink()

        self.assertIn("missing-required-file", self._kinds())

    def test_invalid_json_is_rejected(self) -> None:
        self._write("examples/synthetic/case.json", '{"broken": true,}\n')

        self.assertIn("invalid-json", self._kinds())


if __name__ == "__main__":
    unittest.main()
