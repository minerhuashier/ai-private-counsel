from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DECISION_WORKFLOW = REPOSITORY_ROOT / "docs" / "decision-workflow.md"
GUIDING_PRINCIPLES = REPOSITORY_ROOT / "docs" / "guiding-principles.md"
DECISION_LOG = (
    REPOSITORY_ROOT
    / "examples"
    / "decision-path"
    / "decision-log.template.md"
)


class DecisionWorkflowTests(unittest.TestCase):
    def test_decision_workflow_is_bilingual_and_has_seven_gates(self) -> None:
        text = DECISION_WORKFLOW.read_text(encoding="utf-8")

        for phrase in (
            "# 从迷茫到可提交：AI 协助把维权诉求变成诉讼路径",
            "# From Confusion to Filing: AI-Assisted Translation of a Claim into a Litigation Path",
            "第一关：证据关口",
            "第二关：法律事实关口",
            "第三关：法律关系关口",
            "第四关：责任主体关口",
            "第五关：管辖权关口",
            "第六关：法律与文书关口",
            "第七关：退回修正关口",
            "## Gate 1: Evidence",
            "## Gate 2: Legal Facts",
            "## Gate 3: Legal Relationship",
            "## Gate 4: Responsible Party",
            "## Gate 5: Jurisdiction",
            "## Gate 6: Law and Drafting",
            "## Gate 7: Return and Correction",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_workflow_keeps_human_authority_and_procedural_precision(self) -> None:
        text = DECISION_WORKFLOW.read_text(encoding="utf-8")

        for phrase in (
            "AI 的价值集中在扩大检索范围、持续整理、发现矛盾和生成候选方案；本人负责确认事实、选择路径、承担程序行为和最终后果。",
            "AI 是协助阅读协议和提出候选，不是自动“发现被告”",
            "立案被退回不是败诉，也不表示法院已经评价了实体请求。",
            "正式立案、程序转换和审理通知只表示程序向前推进，不表示法院支持实体请求。",
            "AI could not replace",
            "A returned filing is not a loss",
            "did not establish that the court accepted the merits",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_guiding_principles_are_bilingual_and_delegate_final_choices(self) -> None:
        text = GUIDING_PRINCIPLES.read_text(encoding="utf-8")

        for phrase in (
            "# AI 私人律师项目的指导原则",
            "# Guiding Principles for the AI Private Counsel Project",
            "## 十六项指导原则",
            "## Sixteen Guiding Principles",
            "证据先于结论",
            "官方原文先于模型记忆和搜索摘要",
            "AI 生成的是待审草稿，不是法律行为",
            "程序节点不等于实体结果",
            "人是价值判断和责任的最终节点",
            "Evidence Before Conclusion",
            "Official Text Before Model Memory and Search Snippets",
            "AI Output Is a Draft for Review, Not a Legal Act",
            "Procedural Events Are Not Substantive Outcomes",
            "The Human Is the Final Node for Values and Responsibility",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_decision_log_template_requires_sources_and_human_approval(self) -> None:
        text = DECISION_LOG.read_text(encoding="utf-8")

        for phrase in (
            "法律关系候选",
            "责任主体候选",
            "管辖比较",
            "法律与诉请映射",
            "外部动作与批准",
            "没有明确批准时写 `none`",
            "Candidate Legal Relationships",
            "Candidate Responsible Parties",
            "Jurisdiction Comparison",
            "Law and Claim Mapping",
            "External Acts and Approval",
            "Write `none` when no explicit approval exists.",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_links_resolve(self) -> None:
        documents = (DECISION_WORKFLOW, GUIDING_PRINCIPLES, DECISION_LOG)

        for document in documents:
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
