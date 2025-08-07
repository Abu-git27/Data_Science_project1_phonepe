# 📊 PhonePe Pulse Dashboard

An interactive data visualization dashboard built with **Streamlit**, showcasing insights from the PhonePe Pulse dataset including transaction trends, user behavior, device usage, and insurance coverage. MySQL is used for structured data storage and Plotly for rich visuals.

---

## 📁 Project Structure

```
phone_pe_project_original/
├── dashboard/                         # Streamlit dashboard modules
│   ├── main_dashboard.py              # Main dashboard interface (Streamlit UI)
│   ├── scenario_1_transaction_dynamics.py
│   ├── scenario_2_device_engagement.py
│   ├── scenario_3_insurance_growth.py
│   ├── scenario_4_market_expansion.py
│   ├── scenario_5_user_engagement.py
│   └── map.py                         # Map visualization module

├── data/                              # Raw PhonePe Pulse datasets
│   ├── (raw JSONs or PhonePe Pulse structure, optional by state/year)

├── *.py                               # Data extraction & transformation scripts
│   ├── agg_transaction.py             # Extract & clean aggregate transaction data
│   ├── agg_user.py                    # Extract & clean aggregate user data
│   ├── agg_insurance.py               # Extract & clean insurance data
│   ├── map_transaction.py             # Extract map-based transaction data
│   ├── map_user.py                    # Extract map-based user data
│   ├── map_insurance.py               # Extract map-based insurance data
│   ├── top_transaction.py             # Extract top transaction data
│   ├── top_user.py                    # Extract top user data
│   ├── top_insurance.py               # Extract top insurance data
│   └── load_csvs_to_mysql.py          # Loads all processed CSVs into MySQL

├── *.csv                              # Cleaned/processed CSVs ready for dashboard/SQL
│   ├── agg_transaction.csv
│   ├── agg_user.csv
│   ├── agg_insurance.csv
│   ├── map_transaction.csv
│   ├── map_user.csv
│   ├── map_insurance.csv
│   ├── top_transaction.csv
│   ├── top_user.csv
│   ├── top_insurance.csv
│   └── device_user.csv

├── phonepe_logo.png                   # Logo used in the Streamlit dashboard

├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore file
├── venv/, .venv/                      # Virtual environments (ignored by Git)

```

---

## ✅ Features

- 📊 Scenario-based dashboards:
  - Transaction Dynamics
  - Device Engagement
  - Insurance Growth
  - Market Expansion
  - User Engagement
- 🗺️ Geo-spatial visualizations with Plotly
- 📁 MySQL integration for dynamic queries
- ⚡ Interactive UI with dropdowns, filters, and charts

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd phone_pe_project_original
```

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run dashboard/main_dashboard.py
```

---

## 🧪 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- MySQL
- Option Menu UI Plugin

---

## 👨‍💻 Author

- **Name:** Abu Shakeer  
- **Degree:** M.Sc. Computer Science  
- **Skills:** Python, MySQL, Data Science, Streamlit, Flutter, Machine Learning

---

## 📜 License

This project is for educational purposes only.