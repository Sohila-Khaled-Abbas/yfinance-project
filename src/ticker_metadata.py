"""
Fetches company metadata (sector, industry, market cap, etc.)
for given tickers using yfinance and saves them to processed/tickers.csv.
"""

import os
import pandas as pd
import yfinance as yf
import config, utils

def fetch_ticker_metadata(tickers: list[str]) -> pd.DataFrame:
    """
    Fetch company info for each ticker from yfinance.
    
    Parameters
    ----------
    tickers : list[str]
        List of stock ticker symbols.
    
    Returns
    -------
    pd.DataFrame
        DataFrame containing ticker metadata.
    """
    records = []

    for ticker in tickers:
        try:
            info = yf.Ticker(ticker).info
            records.append({
                "Ticker": ticker,
                "Company Name": info.get("longName"),
                "Sector": info.get("sector"),
                "Industry": info.get("industry"),
                "Market Cap": info.get("marketCap"),
                "Country": info.get("country")
            })
        except Exception as e:
            utils.get_logger().warning(f"Failed to fetch metadata for {ticker}: {e}")
            records.append({
                "Ticker": ticker,
                "Company Name": None,
                "Sector": None,
                "Industry": None,
                "Market Cap": None,
                "Country": None
            })
    
    return pd.DataFrame(records)


def save_ticker_metadata(df: pd.DataFrame, filename: str = "tickers.csv") -> None:
    """
    Save ticker metadata to processed/ folder.
    """
    processed_path = os.path.join(config.PROCESSED_DIR, filename)
    os.makedirs(config.PROCESSED_DIR, exist_ok=True)
    df.to_csv(processed_path, index=False)
    utils.get_logger().info(f"Ticker metadata saved to {processed_path}")


if __name__ == "__main__":
    tickers = config.TICKERS
    df_meta = fetch_ticker_metadata(tickers)
    save_ticker_metadata(df_meta)
