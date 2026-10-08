from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_skill_exists():
    assert (ROOT / "skills/cv-pro-max/SKILL.md").exists()

def test_core_rules_exist():
    text = (ROOT / "skills/cv-pro-max/SKILL.md").read_text()
    assert "Truth first" in text
    assert "Question Engine" in text
    assert "ATS first" in text