import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def pick_numeric_cols(df: pd.DataFrame, max_cols=3):
    """
    Pick meaningful numeric columns, excluding ID-like fields.
    """
    candidates = []
    for col in df.select_dtypes(include=["number"]).columns:
        name = col.lower()
        if "id" in name or "objectid" in name:
            continue
        candidates.append(col)
    return candidates[:max_cols]

def plot_numeric_hists(df: pd.DataFrame, out_dir: Path, cols):
    out_dir.mkdir(parents=True, exist_ok=True)
    for col in cols:
        plt.figure()
        plt.hist(df[col].dropna(), bins=30)
        plt.title(f"Distribution: {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig(out_dir / f"hist_{col}.png", bbox_inches="tight")
        plt.close()

def plot_missing_top10(missing_df: pd.DataFrame, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    top = missing_df.sort_values("missing_pct", ascending=False).head(10)

    plt.figure()
    plt.bar(top["column"], top["missing_pct"])
    plt.title("Top 10 Columns by Missing Percentage")
    plt.xlabel("Column")
    plt.ylabel("Missing %")
    plt.xticks(rotation=75, ha="right")
    plt.savefig(out_dir / "missing_top10.png", bbox_inches="tight")
    plt.close()
