from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
from tenacity import retry, wait_exponential, stop_after_attempt
import config
import utils

LOG = utils.LOG

@retry(wait=wait_exponential(min=2, max=30), stop=stop_after_attempt(3))
def fetch_yf(tickers=None, days_back=None) -> pd.DataFrame:
    tickers = tickers or config.TICKERS
    days_back = days_back or config.DAYS_BACK
    end = datetime.today()
    start = end - timedelta(days=days_back)
    LOG.info(f"Fetching {tickers} from {start.date()} to {end.date()}")
    data = yf.download(tickers, start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d"), group_by="ticker", auto_adjust=False, threads=True, progress=False)
    if data.empty:
        raise RuntimeError("No data returned from yfinance")
    return data
