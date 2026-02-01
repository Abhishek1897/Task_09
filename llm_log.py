import json
from datetime import datetime
from pathlib import Path

def log_prompt(path: Path, prompt: str, notes: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "prompt": prompt,
            "notes": notes
        }) + "\n")

def build_hypothesis_prompt(ground_truth: str) -> str:
    return f"""
Rules:
- Do not invent numbers
- Generate hypotheses only
- Propose validation steps
- Communicate uncertainty

Ground truth:
{ground_truth}
""".strip()
