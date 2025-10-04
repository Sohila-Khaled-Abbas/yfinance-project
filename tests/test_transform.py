import pandas as pd
from src.transform import tidy_and_features

def test_tidy_and_features_minimal():
    # Construct minimal yfinance-like structure for single ticker
    idx = pd.to_datetime(["2024-01-01","2024-01-02","2024-01-03"])
    df = pd.DataFrame({
        ("AAPL","Open"): [100, 101, 102],
        ("AAPL","High"): [101, 102, 103],
        ("AAPL","Low"): [99, 100, 101],
        ("AAPL","Close"): [100, 101, 102],
        ("AAPL","Adj Close"): [100, 101, 102],
        ("AAPL","Volume"): [1000, 1100, 1200],
    }, index=idx)
    out = tidy_and_features(df)
    assert "Return" in out.columns
    assert out["Ticker"].nunique() == 1
