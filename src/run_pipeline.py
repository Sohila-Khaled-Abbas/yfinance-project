import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.extract import fetch_yf
from src.transform import tidy_and_features
from src.load import save_parquet
from src import config, utils

LOG = utils.LOG

def main():
    raw = fetch_yf()
    df = tidy_and_features(raw)
    save_parquet(df)

if __name__ == "__main__":
    main()
