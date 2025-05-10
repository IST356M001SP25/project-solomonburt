# visualization.py
import pandas as pd
import plotly.express as px
import streamlit as st

def create_line_chart(df, pollutant):
    """
    Creates an interactive line chart for a specific pollutant over time.

    Args:
        df (pandas.DataFrame): The DataFrame containing the transformed air quality data.
        pollutant (str): The name of the pollutant to visualize.

    Returns:
        plotly.graph_objects._figure.Figure: The Plotly figure.
    """
    df_filtered = df[df['pollutant'] == pollutant]
    fig = px.line(df_filtered, x='time', y='value', title=f'{pollutant} Levels Over Time')
    fig.update_layout(xaxis_title='Time', yaxis_title=f'Value ({pollutant} unit)')
    return fig

def display_pollutant_charts(df):
    """
    Displays line charts for each air pollutant.

    Args:
        df (pandas.DataFrame): The DataFrame containing the transformed air quality data.
    """
    if df is not None:
        pollutants = df['pollutant'].unique()
        st.subheader("Air Quality Trends")
        for pollutant in pollutants:
            fig = create_line_chart(df, pollutant)
            st.plotly_chart(fig)
    else:
        st.warning("No data available to display charts.")

if __name__ == "__main__":
    # Example usage within a Streamlit context (for demonstration)
    st.title("Air Quality Visualization (Example)")
    from data_transformation import load_data_from_cache, transform_air_quality_data
    raw_df = load_data_from_cache()
    transformed_df = transform_air_quality_data(raw_df)
    display_pollutant_charts(transformed_df)