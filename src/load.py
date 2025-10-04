from pathlib import Path
import pandas as pd
import config, utils

LOG = utils.LOG

def save_parquet(df: pd.DataFrame, path: Path = None) -> Path:
    path = path or config.PROCESSED_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    LOG.info(f"Saved {len(df):,} rows to {path}")
    return path
