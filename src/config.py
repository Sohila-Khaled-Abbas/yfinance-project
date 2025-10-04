from pathlib import Path
from datetime import timedelta

ROOT = Path(__file__).resolve().parents[1]

# Tickers & window
TICKERS = ["AAPL", "MSFT", "GOOGL"]
DAYS_BACK = 365

# Paths
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_PATH = PROCESSED_DIR / "finance_latest.parquet"

# Prefect / scheduling defaults
SCHEDULE = {"interval_days": 1}  # adjust as needed

# Create paths if missing at runtime
for p in (RAW_DIR, PROCESSED_DIR):
    p.mkdir(parents=True, exist_ok=True)
