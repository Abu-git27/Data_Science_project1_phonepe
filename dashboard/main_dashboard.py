import sys
import os

# Add parent directory to sys.path to access 'dashboard' module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from streamlit_option_menu import option_menu

# Import scenario modules
import dashboard.scenario_1_transaction_dynamics as s1
import dashboard.scenario_2_device_engagement as s2
import dashboard.scenario_3_insurance_growth as s3
import dashboard.scenario_4_market_expansion as s4
import dashboard.scenario_5_user_engagement as s5
import dashboard.map as m

# --- Set Page Configuration ---
st.set_page_config(page_title="PhonePe Pulse Dashboard", layout="wide")

# --- Load Logo Safely ---
logo_path = os.path.join(os.path.dirname(__file__), "phonepe_logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=120)
else:
    st.warning("Logo image 'phonepe_logo.png' not found in app directory.")

# --- Title ---
st.title("PhonePe Pulse Dashboard")

# --- Sidebar Menu ---
with st.sidebar:
    selected = option_menu(
        menu_title="MENU",
        options=["Home", "Scenarios", "Map", "About Project", "About Author"],
        icons=["house", "layers", "map", "file-bar-graph", "person"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )

# --- Home Section ---
if selected == "Home":
    st.header("Welcome to PhonePe Pulse Dashboard")
    st.markdown(
        """
        Explore detailed visualizations derived from PhonePe Pulse datasets.  
        Navigate through the sidebar to access various analytical scenarios:
        
        -  Transaction Trends  
        -  Device Engagement  
        -  Insurance Growth  
        -  Market Expansion  
        -  User Engagement  
        -  Map-based View  
        """
    )

# --- Scenarios Section ---
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

# --- Map Section ---
elif selected == "Map":
    m.run()

# --- About Project Section ---
elif selected == "About Project":
    st.header("About the Project")
    st.markdown("""
    This interactive dashboard was built using **PhonePe Pulse** data to explore India's digital payments ecosystem.

    ###  Features:
    - Visual breakdown of transaction types and volume
    - User behavior trends by device
    - Growth in digital insurance coverage
    - Market penetration across regions
    - Real-time choropleth map view

    ###  Technologies Used:
    - Python, Streamlit
    - Pandas, Plotly
    - MySQL (for structured storage)
    
    **Author**: Abu Shakeer (M.Sc. Computer Science)
    """)

# --- About Author Section ---
elif selected == "About Author":
    st.header("About the Author")
    st.markdown("""
    **Name**: Abu Shakeer  
    **Education**: M.Sc. in Computer Science  
    **Skills**:
    - Python, Streamlit, MySQL, Pandas
    - Flutter, Machine Learning, Data Science  
      
    **Objective**:  
    To create impactful, data-driven solutions and help others learn and grow with technology.

    *Thank you for visiting the dashboard!*
    """)
