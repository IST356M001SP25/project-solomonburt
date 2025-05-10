# api_extraction.py
import requests
import json
import os

CACHE_DIR = "cache"
AIR_QUALITY_API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"  # Confirmed URL

def fetch_air_quality_data(latitude, longitude):
    """
    Fetches air quality data for a given latitude and longitude from the Open-Meteo API.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.

    Returns:
        dict or None: A dictionary containing the air quality data if successful, None otherwise.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["carbon_monoxide", "nitrogen_dioxide", "sulphur_dioxide", "ozone", "pm10", "pm2_5"],
        "timezone": "America/New_York"  # Adjust as needed
    }
    try:
        response = requests.get(AIR_QUALITY_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
        return None

def save_data_to_cache(data, filename="air_quality_data.json"):
    """
    Saves the fetched data to a JSON file in the cache directory.

    Args:
        data (dict): The data to save.
        filename (str, optional): The name of the file. Defaults to "air_quality_data.json".
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    filepath = os.path.join(CACHE_DIR, filename)
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filepath}")
    except IOError as e:
        print(f"Error saving data to cache: {e}")

if __name__ == "__main__":
    # Example usage: Fetch data for Brock Hall, Maryland
    brock_hall_lat = 38.9897
    brock_hall_lon = -76.9378
    air_quality_data = fetch_air_quality_data(brock_hall_lat, brock_hall_lon)
    if air_quality_data:
        save_data_to_cache(air_quality_data)