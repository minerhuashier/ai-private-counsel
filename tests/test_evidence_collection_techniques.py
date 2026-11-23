from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TECHNIQUES = REPOSITORY_ROOT / "docs" / "evidence-collection-techniques.md"


class EvidenceCollectionTechniquesTests(unittest.TestCase):
    def test_document_is_bilingual_and_covers_four_technical_layers(self) -> None:
        text = TECHNIQUES.read_text(encoding="utf-8")

        for phrase in (
            "# 证据收集的技术、方法与指导原则：从页面到可核验证据链",
            "# Technology, Methods, and Guiding Principles for Evidence Collection: From Page Capture to a Verifiable Evidence Chain",
            "访问与抓取层",
            "完整性与保管层",
            "数字化与结构化层",
            "核验与法律映射层",
            "Access and Capture",
            "Integrity and Custody",
            "Digitization and Structure",
            "Verification and Legal Mapping",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_method_preserves_user_control_and_technical_traceability(self) -> None:
        text = TECHNIQUES.read_text(encoding="utf-8")

        for phrase in (
            "用户本人登录",
            "只读采集",
            "SHA-256",
            "本地离线录音转写",
            "分页索引与时间线",
            "官方法律来源登记",
            "`observed`",
            "`extracted`",
            "`inferred`",
            "`unverified`",
            "`SOURCE_CONFLICT`",
            "`blocked_captcha`",
            "`login_required`",
            "User signs in",
            "Read-only capture",
            "Local offline audio transcription",
            "Official legal-source register",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_principles_and_limits_fail_closed(self) -> None:
        text = TECHNIQUES.read_text(encoding="utf-8")

        for phrase in (
            "原件优先",
            "本人认证",
            "只读和最小权限",
            "遇到访问控制即停止",
            "哈希只能证明文件一致",
            "截图不等于完整后台记录",
            "OCR 不等于原文",
            "AI 摘要更不等于证据",
            "不得绕过验证码",
            "Originals first",
            "User-controlled authentication",
            "Read-only and least privilege",
            "Stop at access controls",
            "A hash proves file consistency",
            "A screenshot is not a complete back-office record",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_relative_links_resolve(self) -> None:
        text = TECHNIQUES.read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", text)
        relative_links = [
            link
            for link in links
            if "://" not in link and not link.startswith(("mailto:", "#"))
        ]

        for link in relative_links:
            with self.subTest(link=link):
                target = (TECHNIQUES.parent / link).resolve()
                self.assertTrue(target.exists(), f"Missing link target: {link}")


if __name__ == "__main__":
    unittest.main()
