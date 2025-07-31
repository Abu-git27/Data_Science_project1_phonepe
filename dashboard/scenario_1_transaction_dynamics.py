import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

sns.set(style="whitegrid")

def run():
    st.subheader("Scenario 1: Transaction Dynamics")

    # Load data
    try:
        df = pd.read_csv("agg_transaction.csv")
    except FileNotFoundError:
        st.error("'agg_transaction.csv' not found in the root directory.")
        return

    # Combine Year and Quarter for trend analysis
    df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)

    grouped = df.groupby(['State', 'YearQuarter', 'Transaction_type']).agg({
        'Transaction_count': 'sum',
        'Transaction_amount': 'sum'
    }).reset_index()

    ## Q1: Which states show consistent growth?
    st.markdown("### 1. States Showing Consistent Growth in Transaction Count & Amount")
    top_growth_states = df.groupby('State')['Transaction_count'].sum().sort_values(ascending=False).head(5).index

    fig1, ax1 = plt.subplots(figsize=(15, 5))
    for state in top_growth_states:
        state_data = grouped[grouped['State'] == state].groupby('YearQuarter').sum(numeric_only=True).reset_index()
        ax1.plot(state_data['YearQuarter'], state_data['Transaction_count'], label=state)
    ax1.set_title("Transaction Count Trend - Top 5 States")
    ax1.set_xlabel("Year-Quarter")
    ax1.set_ylabel("Transaction Count")
    ax1.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots(figsize=(15, 5))
    for state in top_growth_states:
        state_data = grouped[grouped['State'] == state].groupby('YearQuarter').sum(numeric_only=True).reset_index()
        ax2.plot(state_data['YearQuarter'], state_data['Transaction_amount'], label=state)
    ax2.set_title("Transaction Amount Trend - Top 5 States")
    ax2.set_xlabel("Year-Quarter")
    ax2.set_ylabel("Transaction Amount (INR)")
    ax2.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    ## Q2: Which payment categories contribute the most?
    st.markdown("### 2. Top Payment Categories by Volume & Value")

    type_summary = df.groupby('Transaction_type')[['Transaction_count', 'Transaction_amount']].sum().sort_values(by='Transaction_count', ascending=False)

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=type_summary.index, y=type_summary['Transaction_count'], ax=ax3)
    ax3.set_title("Transaction Count by Payment Category")
    ax3.set_ylabel("Count")
    ax3.set_xlabel("Transaction Type")
    st.pyplot(fig3)

    fig4, ax4 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=type_summary.index, y=type_summary['Transaction_amount'], ax=ax4)
    ax4.set_title("Transaction Amount by Payment Category")
    ax4.set_ylabel("Amount (INR)")
    ax4.set_xlabel("Transaction Type")
    st.pyplot(fig4)

    ## Q3: States or categories with drops or stagnation
    st.markdown("### 3. States or Categories Showing Drop/Stagnation")

    bottom_states = df.groupby('State')['Transaction_count'].sum().sort_values().head(5).index

    fig5, ax5 = plt.subplots(figsize=(15, 5))
    for state in bottom_states:
        state_data = grouped[grouped['State'] == state].groupby('YearQuarter').sum(numeric_only=True).reset_index()
        ax5.plot(state_data['YearQuarter'], state_data['Transaction_count'], label=state)
    ax5.set_title("Transaction Count - Bottom 5 States")
    ax5.set_xlabel("Year-Quarter")
    ax5.set_ylabel("Transaction Count")
    ax5.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig5)

    ## Q4: Compare top vs bottom performing states
    st.markdown("### 4. Compare Top 5 vs Bottom 5 States")

    combined_states = list(top_growth_states) + list(bottom_states)
    fig6, ax6 = plt.subplots(figsize=(18, 6))
    for state in combined_states:
        state_data = grouped[grouped['State'] == state].groupby('YearQuarter').sum(numeric_only=True).reset_index()
        ax6.plot(state_data['YearQuarter'], state_data['Transaction_amount'], label=state)
    ax6.set_title("Transaction Amount Comparison: Top vs Bottom States")
    ax6.set_xlabel("Year-Quarter")
    ax6.set_ylabel("Amount (INR)")
    ax6.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig6)

    ## Q5: Seasonal or Quarterly Patterns
    st.markdown("### 5. Seasonal/Quarterly Patterns Across Categories")

    quarter_avg = df.groupby(['YearQuarter', 'Transaction_type'])[['Transaction_count']].sum().reset_index()

    fig7 = plt.figure(figsize=(16, 6))
    sns.lineplot(data=quarter_avg, x='YearQuarter', y='Transaction_count', hue='Transaction_type', marker='o')
    plt.title("Quarterly Pattern by Payment Category")
    plt.xlabel("Year-Quarter")
    plt.ylabel("Transaction Count")
    plt.xticks(rotation=45)
    st.pyplot(fig7)

    # Download Option for last chart
    st.markdown("### 📥 Download Last Chart")
    buf = BytesIO()
    fig7.savefig(buf, format="png")
    st.download_button(
        label="Download Seasonal Pattern Chart as PNG",
        data=buf.getvalue(),
        file_name="seasonal_pattern_chart.png",
        mime="image/png"
    )

    st.success("✅ All 5 analysis questions visualized successfully.")
