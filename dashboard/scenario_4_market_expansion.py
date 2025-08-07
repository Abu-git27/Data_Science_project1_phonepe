import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.subheader("Scenario 4: Market Expansion Insights")
    sns.set(style="whitegrid")

    try:
        agg_df = pd.read_csv('agg_transaction.csv')
        map_df = pd.read_csv('map_transaction.csv')
        top_df = pd.read_csv('top_transaction.csv')
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return

    # 1. Top 10 States by Total Transaction Amount
    top_states = agg_df.groupby('State')['Transaction_amount'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_states.values, y=top_states.index, palette='viridis')
    plt.title('** 1.Top 10 States by Total Transaction Amount')
    plt.xlabel('Transaction Amount (INR)')
    plt.ylabel('State')
    plt.tight_layout()
    st.pyplot(plt)

    # 2. Top 10 Districts by Total Transaction Amount
    top_districts = map_df.groupby('District')['TransactionAmount'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_districts.values, y=top_districts.index, palette='magma')
    plt.title('** 2.Top 10 Districts by Transaction Amount')
    plt.xlabel('Transaction Amount (INR)')
    plt.ylabel('District')
    plt.tight_layout()
    st.pyplot(plt)

    # 3. Quarterly Transaction Trend for Top 3 States
    agg_df['YearQuarter'] = agg_df['Year'].astype(str) + '-Q' + agg_df['Quarter'].astype(str)
    top_3_states = top_states.head(3).index
    plt.figure(figsize=(14, 6))
    for state in top_3_states:
        state_data = agg_df[agg_df['State'] == state]
        plt.plot(state_data['YearQuarter'], state_data['Transaction_amount'], label=state)
    plt.title('** 3.Quarterly Transaction Amount Trend (Top 3 States)')
    plt.xlabel('Year-Quarter')
    plt.ylabel('Transaction Amount (INR)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    st.pyplot(plt)

    # 4. Top 10 Pincodes by Transaction Amount
    top_pincodes = top_df.groupby('Pincode')['Transaction_amount'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_pincodes.values, y=top_pincodes.index.astype(str), palette='coolwarm')
    plt.title('** 4.Top 10 Pincodes by Transaction Amount')
    plt.xlabel('Transaction Amount (INR)')
    plt.ylabel('Pincode')
    plt.tight_layout()
    st.pyplot(plt)

    # 5. State-wise Average Transaction Amount per Quarter
    state_quarter_avg = agg_df.groupby(['State', 'Year', 'Quarter'])['Transaction_amount'].mean().reset_index()
    state_quarter_avg['YearQuarter'] = state_quarter_avg['Year'].astype(str) + '-Q' + state_quarter_avg['Quarter'].astype(str)
    pivot_df = state_quarter_avg.pivot(index='YearQuarter', columns='State', values='Transaction_amount')[top_3_states]
    pivot_df.plot(figsize=(14, 6), marker='o')
    plt.title('** 5.Average Transaction Amount per Quarter - Top 3 States')
    plt.xlabel('Year-Quarter')
    plt.ylabel('Average Transaction Amount (INR)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(title='State')
    plt.tight_layout()
    st.pyplot(plt)
