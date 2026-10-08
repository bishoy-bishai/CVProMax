from pathlib import Path

ROOT = Path(__file__).parents[1]
SKILL = ROOT / "skills/cv-pro-max/SKILL.md"
BASE = ROOT / "skills/cv-pro-max"


def read(path):
    return (BASE / path).read_text()


def test_skill_exists():
    assert SKILL.exists()


def test_core_rules_exist():
    text = SKILL.read_text()
    assert "Truth is a hard constraint" in text
    assert "Question Engine" in text
    assert "ATS-first" in text
    assert "CV Optimizer Execution Contract" in text


def test_optimizer_pipeline_exists():
    text = read("references/cv-optimizer-engine.md")
    for marker in [
        "Evidence Mapping",
        "Relevance Decision Engine",
        "Bullet Rewrite Algorithm",
        "Keyword Alignment",
        "Final CV Validation",
        "Change Log Contract",
    ]:
        assert marker in text


def test_keyword_mapping_has_truth_boundary():
    text = read("references/keyword-mapping.md")
    assert "UNSUPPORTED" in text
    assert "Never introduce a technology because it appears in the JD." in text


def test_ats_validation_rejects_fake_scores():
    text = read("references/ats-validation.md")
    assert "Never output a fake ATS score." in text


def test_command_routes_cv_through_optimizer():
    text = read("commands/cv-pro-max.md")
    assert "CV Optimizer Engine" in text
    assert "Keyword Mapping" in text
    assert "Bullet Rewrite Engine" in text
