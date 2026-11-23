from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK = REPOSITORY_ROOT / "docs" / "evidence-collection-playbook.md"
EVIDENCE_DIR = REPOSITORY_ROOT / "examples" / "evidence"
EVIDENCE_README = EVIDENCE_DIR / "README.md"
PLAN_TEMPLATE = EVIDENCE_DIR / "collection-plan.template.md"
RUN_TEMPLATE = EVIDENCE_DIR / "collection-run.template.md"
MATRIX_TEMPLATE = EVIDENCE_DIR / "legal-evidence-matrix.template.md"


class EvidenceCollectionPlaybookTests(unittest.TestCase):
    def test_playbook_is_bilingual_and_covers_all_five_gates(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "# 从一段叙述到可核验证据链：AI 协助取证的五个关口",
            "# From a Narrative to a Verifiable Evidence Chain: Five Gates of AI-Assisted Evidence Collection",
            "关口一：从叙述生成建议证据清单",
            "关口二：用户配合与只读授权",
            "关口三：固定原始材料与页面状态",
            "关口四：数字化为可检索、可回链的 Markdown",
            "关口五：用法律要件反查证据",
            "Gate 1: Generate a proposed evidence list from the narrative",
            "Gate 2: User cooperation and read-only authorization",
            "Gate 3: Preserve originals and page states",
            "Gate 4: Digitize into searchable Markdown with links back to originals",
            "Gate 5: Check the evidence against legal elements",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_historical_channel_and_read_only_boundary_are_explicit(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "早期实际操作使用的是**应用内浏览器**",
            "不是后来才形成的系统 Chrome 操作契约",
            "用户本人预先保持账号登录",
            "只做导航、读取、截图和整理",
            "密码、短信验证码、扫码确认、Cookie、支付密码或恢复码",
            "代为申请退款或售后",
            "确认收货",
            "绕过验证码或访问控制",
            "blocked_captcha",
            "The historical operation used the **in-app browser**",
            "not the later system-Chrome operating contract",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_preservation_and_digitization_keep_links_to_originals(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "31 页连续截图",
            "105 条带时间的消息",
            "逐文件 SHA-256",
            "先 OCR，再逐张视觉复核",
            "本地离线转写",
            "数字化结果不是新的“原件”",
            "`observed`",
            "`extracted`",
            "`inferred`",
            "`unverified`",
            "`SOURCE_CONFLICT`",
            "31 consecutive screenshots",
            "105 timestamped messages",
            "OCR followed by visual review",
            "local offline transcription",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_legal_review_preserves_limits_of_proof(self) -> None:
        text = PLAYBOOK.read_text(encoding="utf-8")

        for phrase in (
            "法律要件反查证据",
            "规范名称、条号、生效版本",
            "页面数据快照不是平台后台数据库导出",
            "支付回单只能证明付款行为",
            "工单页面没有显示处理结论",
            "申请法院调查取证",
            "请求对方提交材料",
            "official text",
            "A page-data snapshot",
            "not a platform database export",
            "court investigation",
            "production of documents",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_templates_are_bilingual_and_include_safety_controls(self) -> None:
        expected_headers = {
            EVIDENCE_README: ("# 证据取证模板", "# Evidence Collection Templates"),
            PLAN_TEMPLATE: ("# 取证计划模板", "# Evidence Collection Plan Template"),
            RUN_TEMPLATE: (
                "# 取证运行记录模板",
                "# Evidence Collection Run Record Template",
            ),
            MATRIX_TEMPLATE: (
                "# 法律要件与证据矩阵模板",
                "# Legal-Elements and Evidence Matrix Template",
            ),
        }

        for path, headers in expected_headers.items():
            text = path.read_text(encoding="utf-8")
            for header in headers:
                with self.subTest(path=path.name, header=header):
                    self.assertIn(header, text)

        plan_text = PLAN_TEMPLATE.read_text(encoding="utf-8")
        run_text = RUN_TEMPLATE.read_text(encoding="utf-8")
        matrix_text = MATRIX_TEMPLATE.read_text(encoding="utf-8")

        for phrase in (
            "建议证据清单",
            "USER_ONLY",
            "PROHIBITED",
            "密码、短信验证码、扫码确认、Cookie",
            "SHA-256",
            "login_required",
            "blocked_captcha",
        ):
            with self.subTest(template="plan", phrase=phrase):
                self.assertIn(phrase, plan_text)

        for phrase in (
            "用户本人完成登录",
            "AI 是否接触密码、验证码或 Cookie：`NO`",
            "页面截图只证明截图时点的显示状态",
            "页面数据快照不是平台后台日志",
            "OCR_UNVERIFIED",
            "待调查取证或责令提交",
        ):
            with self.subTest(template="run", phrase=phrase):
                self.assertIn(phrase, run_text)

        for phrase in (
            "规范名称、条号、版本和施行时间都必须回到官方来源核验",
            "SUFFICIENT / INDIRECT / GAP / HOLD",
            "INVESTIGATION / PRODUCTION_ORDER",
            "官方来源",
            "SHA-256",
        ):
            with self.subTest(template="matrix", phrase=phrase):
                self.assertIn(phrase, matrix_text)

    def test_relative_links_in_evidence_documents_resolve(self) -> None:
        for document in (PLAYBOOK, EVIDENCE_README, PLAN_TEMPLATE, RUN_TEMPLATE, MATRIX_TEMPLATE):
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
