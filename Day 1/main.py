import requests
import pandas as pd
import logging

# Set up logging so you know what happened if it fails
logging.basicConfig(level=logging.INFO)


def fetch_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the website actually worked
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch data: {e}")
        return None


def transform_data(raw_data):
    # Extract only what we need
    return pd.DataFrame([raw_data["current_weather"]])


def save_to_csv(df, filename="weather.csv"):
    df.to_csv(filename, index=False)
    logging.info(f"Data successfully saved to {filename}")


# Main Execution
if __name__ == "__main__":
    API_URL = "https://api.open-meteo.com/v1/forecast?latitude=1.35&longitude=103.82&current_weather=true"

    data = fetch_weather_data(API_URL)
    if data:
        clean_df = transform_data(data)
        save_to_csv(clean_df)