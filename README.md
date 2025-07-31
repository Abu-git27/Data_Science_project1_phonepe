#  PhonePe Pulse Data Analytics Dashboard (Streamlit + MySQL)

##  Overview

This is an end-to-end **Data Analytics and Visualization Dashboard** project built with **Python, Streamlit, MySQL, and Plotly**, focused on deriving business insights from the official [PhonePe Pulse GitHub data](https://github.com/PhonePe/pulse).

The project extracts raw **JSON files**, cleans and transforms them into structured **CSV and MySQL tables**, and presents **interactive dashboards** that simulate PhonePe’s internal insights tools across five unique business scenarios.

---

## Tech Stack

- **Frontend**: Streamlit (interactive UI)
- **Backend**: Python
- **Database**: MySQL
- **Visualization**: Plotly (Choropleth Maps, Bar, Pie charts)
- **Data Source**: PhonePe Pulse GitHub (JSON)
- **Libraries**: `pandas`, `json`, `os`, `mysql-connector-python`, `streamlit`, `plotly`, `streamlit-option-menu`

---

##  Project Workflow

###  1.Data Extraction & Conversion

- Cloned PhonePe Pulse GitHub repository.
- Parsed deeply nested JSON files (transactions, users, devices, insurance).
- Converted into structured CSV format.

### 2.Data Cleaning & Transformation

- Standardized state names (e.g., `Andhra-Pradesh → Andhra Pradesh`)
- Casted columns to proper datatypes (amounts, counts, percentages).
- Combined Year, Quarter, State, and Metric-level data.
- Removed duplicates and zero-valued entries for clarity.

### 3.Data Storage (MySQL Integration)

- Designed and normalized MySQL tables:
  - `transactions`, `users`, `devices`, `insurance`
- Inserted cleaned CSV data into MySQL using `mysql-connector-python`.

### 4.Dashboard Development (Streamlit)

- Built a multi-page dashboard with sidebar navigation.
- Developed 5 scenario-based visualizations using `streamlit-option-menu`.

---

##  Dashboard Scenarios

### 1.Decoding Transaction Dynamics
- Total transactions (amount & count) by state and quarter.
- State-wise choropleth maps for visual transaction analysis.

### 2.Uncovering Device Engagement
- Most used mobile brands per state.
- Bar and pie charts showing brand usage trends.

### 3.Insurance Growth Mapping
- Insurance adoption across states and pincodes.
- Sum assured and policy count visualizations.

### 4.Market Expansion Analysis
- Category-wise transaction volume across quarters.
- Helps track growing and stagnant market sectors.

### 5.User Engagement Insights
- New user registrations and app usage patterns.
- Filters by year, quarter, state, and device brand.

---

## Key Features

- Dynamic filters (Year, Quarter, State, Category)
- GeoJSON-based Choropleth Maps for state-level insights
- Modular and reusable code (scenario-wise files)
- Real-time queries from MySQL for live interaction
- Optimized performance via pre-aggregated views

---

## Project Folder Structure

phone_pe_project_original/
│
├── .venv/                             
├── dashboard/                         
│   ├── __init__.py
│   ├── map.py
│   ├── scenario_1_transaction_dynamics.py
│   ├── scenario_2_device_engagement.py
│   ├── scenario_3_insurance_growth.py
│   ├── scenario_4_market_expansion.py
│   └── scenario_5_user_engagement.py
│
├── data/                              
│
├── agg_insurance.csv                 
├── agg_insurance.py
├── agg_transaction.csv
├── agg_transaction.py
├── agg_user.csv
├── agg_user.py
├── agg_user_by_device.py            
├── device_user.csv
├── device_user.py
├── india_state.geojson              
├── load_csvs_to_mysql.py            
├── main_dashboard.py                
├── map_insurance.csv
├── map_insurance.py
├── map_transaction.csv
├── map_transaction.py
├── map_user.csv
├── map_user.py
├── phonepe_logo.png
├── README.md
├── requirements.txt                 
├── top_insurance.csv
├── top_insurance.py
├── top_transaction.csv
├── top_transaction.py
├── top_user.csv
└── top_user.py

## How to Run Locally

- Clone the repo:

git clone https://github.com/YOUR-USERNAME/phonepe-project.git
cd phonepe-project

- Create virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

- Install requirements:

pip install -r requirements.txt

- Run the Streamlit app:

streamlit run app.py
