from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PIPELINE = REPOSITORY_ROOT / "docs" / "legal-source-pipeline.md"
CAPTURE = REPOSITORY_ROOT / "docs" / "codex-chrome-source-capture.md"
SKILL = REPOSITORY_ROOT / "skills" / "legal-source-archive" / "SKILL.md"
SOURCE_TEMPLATE = (
    REPOSITORY_ROOT
    / "examples"
    / "legal-sources"
    / "source-register.template.md"
)
MATRIX_TEMPLATE = (
    REPOSITORY_ROOT
    / "examples"
    / "legal-sources"
    / "rule-use-matrix.template.md"
)
DOWNLOAD_RUN_TEMPLATE = (
    REPOSITORY_ROOT
    / "examples"
    / "legal-sources"
    / "download-run.template.md"
)


class LegalSourcePipelineTests(unittest.TestCase):
    def test_pipeline_is_bilingual_and_covers_all_three_questions(self) -> None:
        text = PIPELINE.read_text(encoding="utf-8")

        self.assertIn("# 从官方文本到可引用法律", text)
        self.assertIn("# From Official Text to Citable Law", text)
        self.assertIn("让 AI 下载法律法规", text)
        self.assertIn("PDF 法律法规的数字化方法", text)
        self.assertIn("我如何使用这些法律法规", text)
        self.assertIn("Acquire Legal Sources", text)
        self.assertIn("PDFs Were Digitized", text)
        self.assertIn("How the Laws Were Used", text)

    def test_pipeline_lists_public_legal_instrument_names_in_full(self) -> None:
        text = PIPELINE.read_text(encoding="utf-8")

        for title in (
            "《中华人民共和国民法典》",
            "《中华人民共和国消费者权益保护法》",
            "《中华人民共和国电子商务法》",
            "《中华人民共和国旅游法》",
            "《中华人民共和国民事诉讼法》",
            "《网络交易监督管理办法》",
            "《最高人民法院关于审理网络消费纠纷案件适用法律若干问题的规定（一）》",
            "《最高人民法院关于适用〈中华人民共和国民事诉讼法〉的解释》",
            "《最高人民法院关于互联网法院案件管辖的规定》",
        ):
            with self.subTest(title=title):
                self.assertIn(title, text)

    def test_digitization_paths_are_explicit_and_fail_closed(self) -> None:
        text = PIPELINE.read_text(encoding="utf-8")

        for phrase in (
            "PDF 文本层",
            "官方 DOCX",
            "官方 HTML",
            "OCR 是最后手段",
            "OCR_UNVERIFIED",
            "SHA-256",
            "版本审查",
            "失败关闭",
            "PDF text layer",
            "OCR only when unavoidable",
            "Quality checks",
            "Fail-Closed",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_skill_contains_workflow_outputs_and_stop_conditions(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        for phrase in (
            "# 法律法规来源存档与数字化",
            "# Legal Source Archival and Digitization",
            "## 输入",
            "## 输出",
            "## 失败关闭",
            "## Inputs",
            "## Outputs",
            "## Fail-Closed Conditions",
            "shasum -a 256",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_chrome_capture_note_is_bilingual_and_auditable(self) -> None:
        text = CAPTURE.read_text(encoding="utf-8")

        for phrase in (
            "# 用系统 Chrome 检索、下载与固定法律法规",
            "# Retrieving and Preserving Legal Sources with System Chrome",
            "codex-chrome-ops",
            "preflight.mjs",
            "ready: true",
            'agent.browsers.get("chrome")',
            'get("extension")',
            "只尝试一次",
            "try `get(\"extension\")` once",
            "最终 URL",
            "final URL",
            "SHA-256",
            "验证码",
            "CAPTCHA",
            "登录",
            "login",
            "覆盖限制",
            "coverage limits",
            "内置浏览器",
            "in-app browser",
            "不能把早期操作追溯改写成系统 Chrome",
            "does not mean that every early step was performed in system Chrome",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_chrome_capture_note_fails_closed_without_bypass(self) -> None:
        text = CAPTURE.read_text(encoding="utf-8")

        for phrase in (
            "chrome_channel_unavailable",
            "blocked_login",
            "blocked_captcha",
            "incomplete_text",
            "source_conflict",
            "不得切换浏览器通道",
            "不得绕过",
            "公开方法不把这种做法推荐为常规路径",
            "do not switch channels without explicit user approval",
            "Never copy browser credentials",
            "is not a recommended public workflow",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_chrome_capture_note_documents_skill_evolution_and_components(
        self,
    ) -> None:
        text = CAPTURE.read_text(encoding="utf-8")

        for phrase in (
            "从 `02-资料下载` 到自研 `codex-chrome-ops`",
            "From `02-Legal-Source-Download` to the self-developed `codex-chrome-ops`",
            "`window.__INITIAL_STATE__`",
            "官方 `control-chrome` 传输层",
            "official `control-chrome` transport",
            "操作契约层",
            "operating-contract layer",
            "`scripts/preflight.mjs`",
            "`references/query-playbook.md`",
            "`references/form-playbook.md`",
            "`references/recovery.md`",
            "不是自研 Chrome 扩展",
            "nor a custom Chrome extension",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_templates_are_bilingual_and_placeholder_only(self) -> None:
        source_text = SOURCE_TEMPLATE.read_text(encoding="utf-8")
        matrix_text = MATRIX_TEMPLATE.read_text(encoding="utf-8")
        run_text = DOWNLOAD_RUN_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("# 法律法规来源登记模板", source_text)
        self.assertIn("# Legal Source Register Template", source_text)
        self.assertIn("<OFFICIAL_URL>", source_text)
        self.assertIn("<FINAL_URL>", source_text)
        self.assertIn("system_chrome / in_app_browser / web_search / http", source_text)
        self.assertIn("<SHA256>", matrix_text)

        self.assertIn("# 法律适用矩阵模板", matrix_text)
        self.assertIn("# Legal-Use Matrix Template", matrix_text)
        self.assertIn("<EVIDENCE_IDS>", matrix_text)

        self.assertIn("# 法律法规下载运行记录模板", run_text)
        self.assertIn("# Legal-Source Download Run Record Template", run_text)
        self.assertIn("RUN-<TYPE>-<NNN>", run_text)
        self.assertIn("ART-<NNN>", run_text)
        self.assertIn("64_LOWERCASE_HEX", run_text)
        self.assertIn("chrome_channel_unavailable", run_text)

    def test_relative_links_in_pipeline_and_skill_resolve(self) -> None:
        for document in (PIPELINE, CAPTURE, SKILL):
            text = document.read_text(encoding="utf-8")
            links = re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", text)
            relative_links = [
                link
                for link in links
                if "://" not in link and not link.startswith(("mailto:", "#"))
            ]

            for link in relative_links:
                with self.subTest(document=document.name, link=link):
                    target = (document.parent / link).resolve()
                    self.assertTrue(target.exists(), f"Missing link target: {link}")


if __name__ == "__main__":
    unittest.main()
