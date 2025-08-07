import streamlit as st
import pandas as pd
import plotly.express as px
import os
import requests

def run():
    st.set_page_config(page_title="India Transaction Map", layout="wide")
    st.title("State-wise Transaction Map of India")
    st.subheader("Visualizing Total PhonePe Transaction Amounts")

    # Load and merge CSVs
    csv_files = [file for file in os.listdir() if file.endswith(".csv")]
    if not csv_files:
        st.warning("No CSV files found in the current directory.")
        return

    all_data = pd.DataFrame()
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            all_data = pd.concat([all_data, df], ignore_index=True)
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
            return

    # Normalize column names
    all_data.columns = all_data.columns.str.strip().str.lower().str.replace(" ", "_")
    if 'state' not in all_data.columns or 'transaction_amount' not in all_data.columns:
        st.error("Each CSV must contain 'State' and 'Transaction_Amount' columns.")
        return

    all_data.rename(columns={'state': 'State', 'transaction_amount': 'Transaction_Amount'}, inplace=True)

    # Standardize state names
    all_data['State'] = all_data['State'].str.replace('-', ' ') \
                                         .str.strip() \
                                         .str.title()

    # Group by state and sum transaction amount
    state_data = all_data.groupby("State", as_index=False)["Transaction_Amount"].sum()

    # Load GeoJSON
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    geojson_data = requests.get(geojson_url).json()

    # Filter only states present in GeoJSON to avoid mapping issues
    geojson_states = [feature["properties"]["ST_NM"] for feature in geojson_data["features"]]
    state_data = state_data[state_data["State"].isin(geojson_states)]

    # Choropleth map
    fig = px.choropleth(
        state_data,
        geojson=geojson_data,
        featureidkey="properties.ST_NM",
        locations="State",
        color="Transaction_Amount",
        color_continuous_scale="Reds",
        labels={'Transaction_Amount': 'Total Transaction ₹'},
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        coloraxis_colorbar=dict(title="Transaction Amount", tickprefix="₹"),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("View Data Table"):
        st.dataframe(state_data)

if __name__ == "__main__":
    run()
