from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
STORY_PATH = REPOSITORY_ROOT / "docs" / "founder-story.md"
README_PATH = REPOSITORY_ROOT / "README.md"


class FounderStoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.story = STORY_PATH.read_text(encoding="utf-8")

    def test_story_has_chinese_and_english_titles(self) -> None:
        self.assertIn("# AI 帮我打官司，最强私人律师上线", self.story)
        self.assertIn(
            "# AI Helps Me Fight My Case: The Ultimate Private Counsel Is Online",
            self.story,
        )

    def test_story_keeps_the_case_procedural_and_undecided(self) -> None:
        self.assertIn("案件仍在法院程序中", self.story)
        self.assertIn("本文不宣称胜诉", self.story)
        self.assertIn("the case is still proceeding through the court", self.story)
        self.assertIn("does not claim a favorable judgment", self.story)

    def test_story_does_not_contain_obvious_direct_identifiers(self) -> None:
        patterns = {
            "email address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            "URL": r"https?://",
            "long numeric identifier": r"(?<!\d)\d{5,}(?!\d)",
            "explicit calendar date": r"(?<!\d)(?:19|20)\d{2}[-/.年]\d{1,2}",
        }
        for label, pattern in patterns.items():
            with self.subTest(label=label):
                self.assertIsNone(re.search(pattern, self.story))

    def test_readme_links_to_the_story_in_both_languages(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")
        self.assertIn("[《AI 帮我打官司，最强私人律师上线》](docs/founder-story.md)", readme)
        self.assertIn(
            "[AI Helps Me Fight My Case: The Ultimate Private Counsel Is Online]"
            "(docs/founder-story.md)",
            readme,
        )


if __name__ == "__main__":
    unittest.main()
