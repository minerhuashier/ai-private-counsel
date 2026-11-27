from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK = REPOSITORY_ROOT / "docs" / "procedural-state-playbook.md"
TEMPLATE = (
    REPOSITORY_ROOT
    / "examples"
    / "procedural-state"
    / "state-register.template.md"
)


class ProceduralStatePlaybookTests(unittest.TestCase):
    def test_playbook_is_bilingual_and_covers_eight_state_axes(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "# 立案之后：用 AI 维护程序状态与准备线上异步审理",
            "# After Filing: Using AI to Maintain Procedural State and Prepare for Asynchronous Online Proceedings",
            "## 八条状态轴",
            "## Eight State Axes",
            "案件身份",
            "程序类型",
            "费用",
            "送达",
            "期限",
            "证据",
            "审理",
            "文书与批准",
            "Case identity",
            "Procedure type",
            "Fees",
            "Service",
            "Deadlines",
            "Evidence",
            "Hearing",
            "Documents and approval",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_conflicts_and_payment_nodes_fail_closed(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "`SOURCE_CONFLICT`",
            "`observed`",
            "`corroborated`",
            "`conflict`",
            "`stale`",
            "`unverified`",
            "`closed`",
            "银行侧支付成功，法院侧入账状态待核实；在核实前不得重复缴纳。",
            "The bank-side payment succeeded; court-side reconciliation remains unverified; do not pay again before verification.",
            "正式文书未提到某个旧期限，不等于该期限当然改变",
            "A formal document does not mention an older deadline. That silence does not prove the deadline changed",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_async_hearing_keeps_window_stage_and_human_action_separate(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "线上异步审理不是“整段时间实时在线”",
            "一个审理窗口不等于要求当事人从开始到结束一直在线",
            "保存提交回执",
            "未经批准不处分权利",
            "Asynchronous Online Proceedings Are Not",
            "A hearing window is not a requirement to remain online from start to finish",
            "Save submission receipts",
            "Do not dispose of rights without approval",
            "程序节点写成实体胜负",
            "convert a procedural event into a substantive outcome",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_template_requires_sources_dates_and_approval(self) -> None:
        text = TEMPLATE.read_text(encoding="utf-8")

        for phrase in (
            "# 程序状态登记模板",
            "# Procedural State Register Template",
            "事件时间",
            "来源时间",
            "抓取时间",
            "SHA-256",
            "可证明范围",
            "来源冲突",
            "没有明确批准时写 `none`",
            "银行侧支付成功；法院侧入账状态待核实；核实前不重复缴纳。",
            "Event time",
            "Source time",
            "Capture time",
            "Proven scope",
            "Write `none` when no explicit approval exists.",
            "The bank-side payment succeeded; court-side reconciliation remains unverified; do not pay again before verification.",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_relative_links_resolve(self) -> None:
        for document in (
            PLAYBOOK,
            TEMPLATE,
            REPOSITORY_ROOT
            / "examples"
            / "procedural-state"
            / "README.md",
        ):
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
