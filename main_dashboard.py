import streamlit as st
from streamlit_option_menu import option_menu
import dashboard.scenario_1_transaction_dynamics as s1
import dashboard.scenario_2_device_engagement as s2
import dashboard.scenario_3_insurance_growth as s3
import dashboard.scenario_4_market_expansion as s4
import dashboard.scenario_5_user_engagement as s5
import dashboard.map as m

st.set_page_config(page_title="PhonePe Pulse Dashboard", layout="wide")

st.image("phonepe_logo.png", width=120)
st.title("PhonePe Pulse Dashboard")

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="MENU",
        options=["Home", "Scenarios", "Map", "About Project", "About Author"],
        icons=["house", "layers", "map", "file-bar-graph", "person"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )

# Home Section
if selected == "Home":
    st.header("Welcome to PhonePe Pulse Dashboard")
    st.markdown(
        """
        This dashboard presents insights derived from PhonePe Pulse datasets. Navigate through different scenarios to explore:
        - Transaction Dynamics
        - Device Engagement
         and more.
        """
    )

# Scenarios Section
elif selected == "Scenarios":
    scenario = st.selectbox(
        "Select a Scenario to Explore",
        (
            "1. Transaction Dynamics",
            "2. Device Engagement",
            "3. Insurance Growth",
            "4. Market Expansion",
            "5. User Engagement"
        )
    )

    if scenario.startswith("1."):
        s1.run()
    elif scenario.startswith("2."):
        s2.run()
    elif scenario.startswith("3."):
        s3.run()
    elif scenario.startswith("4."):
        s4.run()
    elif scenario.startswith("5."):
        s5.run()

# Map Section
elif selected == "Map":
    m.run()

# About Project Section
elif selected == "About Project":
    st.header("About the Project")
    st.markdown("""
    This dashboard was created as part of the PhonePe Pulse data analysis project. It offers insights on:
    - Transaction Dynamics
    - Device Engagement
    - Insurance Growth
    - Market Expansion
    - User Engagement

    **Technologies Used**: Python, Streamlit, Pandas, Plotly, MySQL  
    **Author**: Abu Shakeer (M.Sc. Computer Science)
    """)

# About Author Section
elif selected == "About Author":
    st.header("About the Author")
    st.markdown("""
    - **Name**: Abu Shakeer  
    - **Education**: M.Sc. in Computer Science
                
    *Thank you for visiting the dashboard!*
    """)
