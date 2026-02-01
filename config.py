from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = PROJECT_ROOT / "data_raw"
DATA_CLEAN = PROJECT_ROOT / "data_clean"
DATA_ANALYZED = PROJECT_ROOT / "data_analyzed"

OUTPUTS = PROJECT_ROOT / "outputs"
FIGURES = OUTPUTS / "figures"
TABLES = OUTPUTS / "tables"
REPORTS = OUTPUTS / "reports"

PROMPTS_DIR = PROJECT_ROOT / "prompts"
PROMPT_LOG = PROMPTS_DIR / "prompt_log.jsonl"


def ensure_dirs():
    """
    Create all required directories if they do not exist.
    """
    for p in [
        DATA_RAW,
        DATA_CLEAN,
        DATA_ANALYZED,
        OUTPUTS,
        FIGURES,
        TABLES,
        REPORTS,
        PROMPTS_DIR,
    ]:
        p.mkdir(parents=True, exist_ok=True)
