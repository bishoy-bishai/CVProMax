from pathlib import Path
import json

ROOT = Path(__file__).parents[1]
REQUIRED = [
    ".claude-plugin/plugin.json",
    "README.md",
    "skills/cv-pro-max/SKILL.md",
    "skills/cv-pro-max/commands/cv-pro-max.md",
]

def main():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        raise SystemExit(f"Missing required files: {missing}")
    plugin = json.loads((ROOT / REQUIRED[0]).read_text())
    assert plugin["name"] == "cv-pro-max"
    print("CVProMax validation passed.")

if __name__ == "__main__":
    main()