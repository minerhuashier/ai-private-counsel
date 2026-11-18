from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_DIR = REPOSITORY_ROOT / "docs" / "protocols"


class ProtocolDocumentTests(unittest.TestCase):
    def test_protocol_registry_contains_all_thirteen_entries(self) -> None:
        text = (PROTOCOL_DIR / "README.md").read_text(encoding="utf-8")

        for number in range(1, 14):
            self.assertIn(f"P-{number:02d}", text)

        self.assertIn("13 个协议条目", text)
        self.assertIn("13 protocol entries", text)

    def test_truth_five_is_explicitly_proposed(self) -> None:
        text = (PROTOCOL_DIR / "truth-five-protocol.md").read_text(encoding="utf-8")

        self.assertIn("状态：`PROPOSED / 本次首次书面提出`", text)
        self.assertIn("Status: `PROPOSED / first written in this document`", text)
        self.assertIn("此前没有对应的正式项目文件", text)
        self.assertIn("No formal project document named \"Truth Five\" existed", text)

    def test_aep_is_described_as_external(self) -> None:
        text = (PROTOCOL_DIR / "aep-adoption.md").read_text(encoding="utf-8")

        self.assertIn("不是本项目原创", text)
        self.assertIn("not project-authored", text)
        self.assertIn("外部执行协议", text)
        self.assertIn("external execution protocol", text)

    def test_protocol_documents_have_chinese_and_english_sections(self) -> None:
        expected_headers = {
            "README.md": ("# 协议总表", "# Protocol Registry"),
            "anti-hallucination-protocol.md": (
                "# 防止幻觉协议",
                "# Anti-Hallucination Protocol",
            ),
            "truth-five-protocol.md": (
                "# “真实五问”协议",
                "# Truth Five Protocol",
            ),
            "aep-adoption.md": (
                "# AEP 3.1 采用说明",
                "# AEP 3.1 Adoption Note",
            ),
            "agent-configuration.md": (
                "# 本项目如何初始化 Agent 配置",
                "# How This Project Initializes Agent Configuration",
            ),
        }

        for filename, headers in expected_headers.items():
            with self.subTest(filename=filename):
                text = (PROTOCOL_DIR / filename).read_text(encoding="utf-8")
                for header in headers:
                    self.assertIn(header, text)

    def test_protocol_registry_relative_links_exist(self) -> None:
        registry = PROTOCOL_DIR / "README.md"
        text = registry.read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", text)

        relative_links = [
            link for link in links if "://" not in link and not link.startswith("mailto:")
        ]
        self.assertGreater(len(relative_links), 0)

        for link in relative_links:
            with self.subTest(link=link):
                target = (registry.parent / link).resolve()
                self.assertTrue(target.is_file(), f"Missing protocol link target: {link}")


if __name__ == "__main__":
    unittest.main()
