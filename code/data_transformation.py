# data_transformation.py
import pandas as pd
import os
import json

CACHE_DIR = "cache"

def load_data_from_cache(filename="air_quality_data.json"):
    """
    Loads data from a JSON file in the cache directory into a Pandas DataFrame.

    Args:
        filename (str, optional): The name of the file. Defaults to "air_quality_data.json".

    Returns:
        pandas.DataFrame or None: A DataFrame containing the loaded data if successful, None otherwise.
    """
    filepath = os.path.join(CACHE_DIR, filename)
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data['hourly'])
        df['time'] = pd.to_datetime(df['time'])
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
        return None
    except KeyError as e:
        print(f"Error: Missing key in JSON data: {e}")
        return None

def transform_air_quality_data(df):
    """
    Transforms the air quality DataFrame to a more usable format.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.DataFrame: The transformed DataFrame.
    """
    if df is None:
        return None
    # Melt the DataFrame to have a long format for easier plotting
    df_melted = df.melt(id_vars=['time'], var_name='pollutant', value_name='value')
    return df_melted

if __name__ == "__main__":
    # Example usage: Load and transform data
    air_quality_df_raw = load_data_from_cache()
    if air_quality_df_raw is not None:
        air_quality_df_transformed = transform_air_quality_data(air_quality_df_raw)
        if air_quality_df_transformed is not None:
            print(air_quality_df_transformed.head())