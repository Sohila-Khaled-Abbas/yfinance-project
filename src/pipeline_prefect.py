"""
Defines Prefect flow for fetching financial data (prices + metadata)
and saving outputs for Power BI.
"""

import prefect
from prefect import task, Flow
import pandas as pd
from src import config, utils
from src import extract, transform, load, ticker_metadata

logger = utils.get_logger("pipeline_prefect")

# -------------------------------
# Tasks
# -------------------------------

@task
def extract_prices_task():
    df = extract.fetch_yf(config.TICKERS, config.START_DATE, config.END_DATE)
    return df

@task
def transform_prices_task(df: pd.DataFrame):
    return transform.clean_prices(df)

@task
def load_prices_task(df: pd.DataFrame):
    load.save_prices(df)
    logger.info("Prices data saved successfully.")

@task
def extract_ticker_metadata_task():
    df_meta = ticker_metadata.fetch_ticker_metadata(config.TICKERS)
    return df_meta

@task
def load_ticker_metadata_task(df_meta: pd.DataFrame):
    ticker_metadata.save_ticker_metadata(df_meta)
    logger.info("Ticker metadata saved successfully.")


# -------------------------------
# Flow definition
# -------------------------------

with Flow("Finance-Data-Pipeline") as flow:
    # Branch 1: Prices
    prices_raw = extract_prices_task()
    prices_clean = transform_prices_task(prices_raw)
    load_prices_task(prices_clean)

    # Branch 2: Ticker metadata
    meta_raw = extract_ticker_metadata_task()
    load_ticker_metadata_task(meta_raw)


if __name__ == "__main__":
    logger.info("Running Prefect pipeline...")
    flow.run()
