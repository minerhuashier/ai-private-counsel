from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = REPOSITORY_ROOT / "examples" / "agent-config"
ARCHITECTURE = REPOSITORY_ROOT / "docs" / "agent-architecture.md"

ROLE_IDS = (
    "civil-contract-lawyer",
    "consumer-ecommerce-lawyer",
    "tourism-contract-lawyer",
    "litigation-procedure-lawyer",
    "evidence-specialist",
    "platform-liability-lawyer",
    "publicity-compliance-lawyer",
)

SKILL_IDS = (
    "media-posting",
    "video-editing",
)


class AgentArchitectureTests(unittest.TestCase):
    def test_architecture_has_chinese_and_english_sections(self) -> None:
        text = ARCHITECTURE.read_text(encoding="utf-8")

        self.assertIn("# Agent 构成与设计理由", text)
        self.assertIn("# Agent Composition and Design Rationale", text)
        self.assertIn("一个主 Agent", text)
        self.assertIn("one master Agent", text)
        self.assertIn("失败关闭", text)
        self.assertIn("Fail-Closed Conditions", text)

    def test_architecture_registers_seven_roles_and_two_skills(self) -> None:
        architecture = ARCHITECTURE.read_text(encoding="utf-8")
        role_contracts = (CONFIG_DIR / "roles.example.yaml").read_text(encoding="utf-8")
        project_example = (CONFIG_DIR / "project.example.yaml").read_text(encoding="utf-8")

        for role_id in ROLE_IDS:
            with self.subTest(role_id=role_id):
                self.assertIn(f"  {role_id}:", role_contracts)
                self.assertIn(f"  {role_id}:", project_example)
                self.assertTrue(
                    any(role_id in line for line in architecture.splitlines()),
                    f"Architecture does not mention {role_id}",
                )

        for skill_id in SKILL_IDS:
            with self.subTest(skill_id=skill_id):
                self.assertIn(skill_id, architecture)
                self.assertIn(f"  {skill_id}:", project_example)

    def test_role_contracts_include_shared_safety_gates(self) -> None:
        text = (CONFIG_DIR / "roles.example.yaml").read_text(encoding="utf-8")

        for required in (
            "official_source_required",
            "evidence_reference_required_for_facts",
            "preserve_originals",
            "redact_personal_data",
            "no_external_action_without_human_approval",
            "stop_conditions",
            "human_approval_required_for",
        ):
            with self.subTest(required=required):
                self.assertIn(required, text)

    def test_configuration_templates_are_explicit_placeholders(self) -> None:
        project_example = (CONFIG_DIR / "project.example.yaml").read_text(encoding="utf-8")
        agents_template = (CONFIG_DIR / "AGENTS.template.md").read_text(
            encoding="utf-8"
        )

        self.assertIn('"<PROJECT_NAME>"', project_example)
        self.assertIn('"<CIVIL_DISPUTE_DOMAIN>"', project_example)
        self.assertIn('"YYYY-MM-DD"', project_example)
        self.assertIn("<项目名称>", agents_template)
        self.assertIn("<Project Name>", agents_template)
        self.assertIn("redact_by_default: true", project_example)

    def test_agent_configuration_links_resolve(self) -> None:
        documents = (
            REPOSITORY_ROOT / "README.md",
            ARCHITECTURE,
            CONFIG_DIR / "README.md",
        )

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
