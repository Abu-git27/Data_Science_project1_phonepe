import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run():
    st.subheader("Scenario 3: Insurance Growth Analysis")
    sns.set(style="whitegrid")

    file_path = 'agg_insurance.csv'
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("File 'agg_insurance.csv' not found.")
        return

    required_cols = {'State', 'Year', 'Quarter', 'Transaction_count', 'Transaction_amount'}
    if not required_cols.issubset(df.columns):
        st.error(f"Missing required columns in the dataset. Required: {required_cols}")
        return

    df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)
    grouped = df.groupby(['State', 'YearQuarter']).agg({
        'Transaction_count': 'sum',
        'Transaction_amount': 'sum'
    }).reset_index()

    # ✅ 1. Top 5 States by Transaction Count Over Time
    top_states = grouped.groupby('State')['Transaction_count'].sum().sort_values(ascending=False).head(5).index
    st.markdown("**1. Top 5 States by Insurance Transaction Count Over Time**")
    plt.figure(figsize=(12, 6))
    for state in top_states:
        data = grouped[grouped['State'] == state]
        plt.plot(data['YearQuarter'], data['Transaction_count'], label=state)
    plt.xticks(rotation=45)
    plt.xlabel("Year-Quarter")
    plt.ylabel("Transaction Count")
    plt.legend()
    st.pyplot(plt)

    # ✅ 2. Top 5 States by Transaction Amount Over Time
    top_states_amt = grouped.groupby('State')['Transaction_amount'].sum().sort_values(ascending=False).head(5).index
    st.markdown("**2. Top 5 States by Insurance Transaction Amount Over Time**")
    plt.figure(figsize=(12, 6))
    for state in top_states_amt:
        data = grouped[grouped['State'] == state]
        plt.plot(data['YearQuarter'], data['Transaction_amount'], label=state)
    plt.xticks(rotation=45)
    plt.xlabel("Year-Quarter")
    plt.ylabel("Transaction Amount")
    plt.legend()
    st.pyplot(plt)

    # ✅ 3. Engagement Ratio = Transaction_amount / Transaction_count per State
    df['EngagementRatio'] = df['Transaction_amount'] / df['Transaction_count']
    ratio_group = df.groupby('State')['EngagementRatio'].mean().sort_values(ascending=False).head(10)
    st.markdown("**3. Engagement Ratio (Amount / Count) – Top 10 States**")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=ratio_group.values, y=ratio_group.index, palette="mako")
    plt.xlabel("Engagement Ratio")
    plt.ylabel("State")
    st.pyplot(plt)

    # ✅ 4. Bottom 5 States by Transaction Amount
    bottom_states_amt = grouped.groupby('State')['Transaction_amount'].sum().sort_values().head(5)
    st.markdown("**4. Bottom 5 States by Insurance Transaction Amount (Total)**")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=bottom_states_amt.values, y=bottom_states_amt.index, palette="rocket")
    plt.xlabel("Transaction Amount (INR)")
    plt.ylabel("State")
    st.pyplot(plt)

    # ✅ 5. Bottom 5 States by Transaction Count
    bottom_states_cnt = grouped.groupby('State')['Transaction_count'].sum().sort_values().head(5)
    st.markdown("**5. Bottom 5 States by Insurance Transaction Count (Total)**")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=bottom_states_cnt.values, y=bottom_states_cnt.index, palette="flare")
    plt.xlabel("Transaction Count")
    plt.ylabel("State")
    st.pyplot(plt)
