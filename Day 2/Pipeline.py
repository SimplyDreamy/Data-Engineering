# Data from https://www.kaggle.com/datasets/jakubkrasuski/global-weather-data-conditions-for-209579-cities

import pandas as pd
import os
import logging


# ---------------- CONFIG ----------------
base_dir = os.path.dirname(os.path.abspath(__file__)) # gets current folder
data_dir = os.path.join(base_dir, "Data")
raw_path = os.path.join(data_dir, "Global Weather Data.csv")
profile_name = "profile.csv"
summary_name = "weather_summary.csv"

dtype_settings = {
    'city_id': 'Int64', #native pandas value, allows for NA w/ Int
    'name': str,
    'state': str,
    'country': str,
    'lon': float,
    'lat': float,
    'temperature': float,
    'pressure': 'Int64',
    'humidity': 'Int64',
    'temp_min': float,
    'temp_max': float,
    'visibility': 'Int64',
    'wind_speed': float,
    'wind_deg': 'Int64',
    'wind_gust': float,
    'clouds_all': 'Int64',
    'weather_main': str,
    'weather_description': str,
    'rain_1h': float,
    'rain_3h': float,
    'snow_1h': float,
    'snow_3h': float,
    'timezone': 'Int64'
}

REQUIRED_COLUMNS = set(dtype_settings.keys())

df = pd.read_csv(raw_path, dtype=dtype_settings)

# ---------------- LOGGING ----------------

logging.basicConfig(level=logging.INFO)

# ---------------- ETL ----------------


def extract(path):
    return pd.read_csv(path, dtype=dtype_settings)


def transform(df):
    logging.info("Transforming data...")

    df.columns = df.columns.str.lower()

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = df.drop_duplicates()

    if "state" in df.columns:
        df = df.drop(columns=["state"])
    df = df.dropna(subset=["name", "country"])

    df["country"] = df["country"].str.strip().str.title()
    df["name"] = df["name"].str.strip().str.title()

    logging.info(f"Final rows: {len(df)}")

    return df

    df.info()
    null_report = df.isnull().sum()  # Count NAs before cleaning
    logging.info(null_report)  # 90% of state is null, gust 20%, only vis,country, and name is low
    df.isna().mean() * 100

def load(df, path):
    logging.info(f"Saving to {path}...")
    df.to_csv(os.path.join(data_dir,summary_name), encoding="utf-8", index=False)



def main():
    try:
        df = extract(raw_path)
        df.describe(include="all").to_csv(os.path.join(data_dir,profile_name))
        df = transform(df)
        load(df, data_dir)

        logging.info("ETL completed successfully")

    except Exception as e:
        logging.error(f"ETL failed: {e}")
        raise


if __name__ == "__main__": #only when directly ran
    main()