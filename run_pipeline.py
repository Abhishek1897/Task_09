import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from src.plots import pick_numeric_cols, plot_numeric_hists, plot_missing_top10



import pandas as pd
from pathlib import Path

from src.config import ensure_dirs, DATA_RAW, DATA_CLEAN, TABLES, FIGURES, PROMPT_LOG
from src.clean import clean_city_streets
from src.analyze import missing_summary, numeric_summary, plot_hist
from src.llm_log import build_hypothesis_prompt, log_prompt


def main():
    print("RUN_PIPELINE STARTED ✅")
    ensure_dirs()

    # Detect raw CSV
    csv_files = list(DATA_RAW.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV found in {DATA_RAW}")

    raw_path = csv_files[0]
    print(f"Using raw file: {raw_path.name}")

    # Load
    df_raw = pd.read_csv(raw_path)
    print("Raw shape:", df_raw.shape)

    # Clean
    df_clean = clean_city_streets(df_raw)
    clean_path = DATA_CLEAN / "city_streets_2011_clean.csv"
    df_clean.to_csv(clean_path, index=False)
    print("Clean shape:", df_clean.shape)

    # Analyze
    ms = missing_summary(df_clean)
    ns = numeric_summary(df_clean)

        # Better plots
    plot_missing_top10(ms, FIGURES)
    best_nums = pick_numeric_cols(df_clean, max_cols=3)
    if best_nums:
        plot_numeric_hists(df_clean, FIGURES, best_nums)


    TABLES.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    ms.to_csv(TABLES / "missing_summary.csv", index=False)
    print("Saved:", TABLES / "missing_summary.csv")

    if not ns.empty:
        ns.to_csv(TABLES / "numeric_summary.csv", index=False)
        print("Saved:", TABLES / "numeric_summary.csv")

        first_num = ns["column"].iloc[0]
        plot_hist(df_clean, first_num, FIGURES / f"hist_{first_num}.png")
        print("Saved:", FIGURES / f"hist_{first_num}.png")
    else:
        print("No numeric columns detected; skipping numeric summary + histogram.")

    # LLM prompt logging
    gt_text = ns.head(10).to_string(index=False) if not ns.empty else "No numeric columns detected."
    prompt = build_hypothesis_prompt(gt_text)

    PROMPT_LOG.parent.mkdir(parents=True, exist_ok=True)
    log_prompt(PROMPT_LOG, prompt, notes="Phase 3 hypothesis generation")

    print("Saved:", PROMPT_LOG)
    print("✅ Pipeline completed successfully")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("❌ Pipeline failed:", repr(e))
        raise
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))



import pandas as pd
from pathlib import Path

from src.config import ensure_dirs, DATA_RAW, DATA_CLEAN, TABLES, FIGURES, PROMPT_LOG
from src.clean import clean_city_streets
from src.analyze import missing_summary, numeric_summary, plot_hist
from src.llm_log import build_hypothesis_prompt, log_prompt


def main():
    print("RUN_PIPELINE STARTED ✅")
    ensure_dirs()

    # Detect raw CSV
    csv_files = list(DATA_RAW.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV found in {DATA_RAW}")

    raw_path = csv_files[0]
    print(f"Using raw file: {raw_path.name}")

    # Load
    df_raw = pd.read_csv(raw_path)
    print("Raw shape:", df_raw.shape)

    # Clean
    df_clean = clean_city_streets(df_raw)
    clean_path = DATA_CLEAN / "city_streets_2011_clean.csv"
    df_clean.to_csv(clean_path, index=False)
    print("Clean shape:", df_clean.shape)

    # Analyze
    ms = missing_summary(df_clean)
    ns = numeric_summary(df_clean)

    TABLES.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    ms.to_csv(TABLES / "missing_summary.csv", index=False)
    print("Saved:", TABLES / "missing_summary.csv")

    if not ns.empty:
        ns.to_csv(TABLES / "numeric_summary.csv", index=False)
        print("Saved:", TABLES / "numeric_summary.csv")

        first_num = ns["column"].iloc[0]
        plot_hist(df_clean, first_num, FIGURES / f"hist_{first_num}.png")
        print("Saved:", FIGURES / f"hist_{first_num}.png")
    else:
        print("No numeric columns detected; skipping numeric summary + histogram.")

    # LLM prompt logging
    gt_text = ns.head(10).to_string(index=False) if not ns.empty else "No numeric columns detected."
    prompt = build_hypothesis_prompt(gt_text)

    PROMPT_LOG.parent.mkdir(parents=True, exist_ok=True)
    log_prompt(PROMPT_LOG, prompt, notes="Phase 3 hypothesis generation")

    print("Saved:", PROMPT_LOG)
    print("✅ Pipeline completed successfully")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("❌ Pipeline failed:", repr(e))
        raise
