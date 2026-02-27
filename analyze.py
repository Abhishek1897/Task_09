from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.isna().sum()
        .to_frame("missing_count")
        .assign(missing_pct=lambda x: (x["missing_count"] / len(df) * 100).round(2))
        .reset_index()
        .rename(columns={"index": "column"})
    )

def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    num_cols = df.select_dtypes(include=["number"]).columns
    if len(num_cols) == 0:
        return pd.DataFrame()
    return df[num_cols].describe().T.reset_index().rename(columns={"index": "column"})

def plot_hist(df: pd.DataFrame, col: str, outpath: Path) -> None:
    plt.figure()
    plt.hist(df[col].dropna(), bins=30)
    plt.title(f"Distribution: {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outpath)
    plt.close()
