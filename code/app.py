# app.py
import streamlit as st
from api_extraction import fetch_air_quality_data, save_data_to_cache
from data_transformation import load_data_from_cache, transform_air_quality_data
from visualization import display_pollutant_charts

st.title("Real-Time Air Quality Dashboard")

st.sidebar.header("Settings")
latitude = st.sidebar.number_input("Latitude", value=38.9897, format="%.4f")
longitude = st.sidebar.number_input("Longitude", value=-76.9378, format="%.4f")

if st.sidebar.button("Fetch and Update Data"):
    with st.spinner("Fetching latest air quality data..."):
        raw_data = fetch_air_quality_data(latitude, longitude)
        if raw_data:
            save_data_to_cache(raw_data)
            st.success("Data updated successfully!")
        else:
            st.error("Failed to fetch air quality data.")

st.subheader("Current Air Quality Data")
air_quality_df_raw = load_data_from_cache()
if air_quality_df_raw is not None:
    st.write(air_quality_df_raw)

    air_quality_df_transformed = transform_air_quality_data(air_quality_df_raw)
    if air_quality_df_transformed is not None:
        display_pollutant_charts(air_quality_df_transformed)
else:
    st.info("No cached data available. Please fetch data using the sidebar.")