import pandas as pd
import numpy as np
from typing import List
import utils

LOG = utils.LOG

def tidy_and_features(raw: pd.DataFrame, sma_windows: List[int] = [20, 50], vol_window: int = 30) -> pd.DataFrame:
    """
    Convert multi-index yfinance output into long tidy DF and compute:
    - Return, LogReturn
    - SMA windows
    - Rolling volatility
    """
    frames = []
    # handle single ticker format (no multiindex)
    if not isinstance(raw.columns, pd.MultiIndex):
        # assume raw is a single-ticker DataFrame with OHLCV cols
        raw.columns = pd.MultiIndex.from_product([["_single"], raw.columns])
    for ticker in raw.columns.levels[0]:
        try:
            df = raw[ticker].copy()
        except Exception:
            LOG.warning(f"{ticker} missing in raw data; skipping")
            continue
        df = df.reset_index().rename(columns={"index": "Date"})
        df["Ticker"] = ticker
        df = df.sort_values("Date")
        df["Return"] = df["Adj Close"].pct_change()
        df["LogReturn"] = np.log(df["Adj Close"]) - np.log(df["Adj Close"].shift(1))
        for w in sma_windows:
            df[f"SMA_{w}"] = df["Adj Close"].rolling(w, min_periods=1).mean()
        df[f"Vol_{vol_window}"] = df["Return"].rolling(vol_window, min_periods=1).std()
        frames.append(df)
    if not frames:
        raise RuntimeError("No frames created in transform")
    out = pd.concat(frames, ignore_index=True)
    return out
