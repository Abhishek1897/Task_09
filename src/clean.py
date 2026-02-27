import pandas as pd

def clean_city_streets(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Drop fully empty rows
    out = out.dropna(how="all")

    # Strip whitespace in all text columns
    for col in out.select_dtypes(include=["object"]).columns:
        out[col] = out[col].astype("string").str.strip()

    return out
