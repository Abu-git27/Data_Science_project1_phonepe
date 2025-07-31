import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run():
    st.subheader("📱 Scenario 2: Device Dominance and User Engagement Analysis")

    sns.set(style="whitegrid")

    file_path = 'device_user.csv'
    if not os.path.exists(file_path):
        st.error(f"❌ File not found: {file_path}")
        return

    df = pd.read_csv(file_path)

    if df.empty:
        st.error("❌ No data found in device_user.csv")
        return

    # ✅ Adjust column name
    required_cols = ['Brand', 'RegisteredUsers', 'State', 'Year', 'Quarter']
    for col in required_cols:
        if col not in df.columns:
            st.error(f"❌ Missing required column: '{col}'")
            return

    # ✅ Clean data
    df = df.dropna(subset=['Brand', 'RegisteredUsers', 'State'])
    df = df[(df['Brand'].str.lower() != 'unknown') & (df['State'].str.lower() != 'unknown')]
    df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)

    # ✅ 1. Top Device Brands by Registered Users
    st.markdown("### ✅ 1. Which device brands have the highest number of registered users?")
    top_registered = df.groupby('Brand')['RegisteredUsers'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_registered.values, y=top_registered.index, palette='crest', ax=ax)
    ax.set_xlabel("Total Registered Users")
    ax.set_ylabel("Device Brand")
    ax.set_title("Top 10 Device Brands by Registered Users")
    st.pyplot(fig)

    # ✅ 2. App Engagement
    st.markdown("### ✅ 2. Which device brands have the highest app engagement (AppOpens)?")
    if 'AppOpens' in df.columns:
        top_opens = df.groupby('Brand')['AppOpens'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=top_opens.values, y=top_opens.index, palette='rocket', ax=ax)
        ax.set_xlabel("Total App Opens")
        ax.set_ylabel("Device Brand")
        ax.set_title("Top 10 Device Brands by App Opens")
        st.pyplot(fig)
    else:
        st.warning("⚠️ 'AppOpens' column not found. Skipping this chart.")

    # ✅ 3. Engagement Ratio
    st.markdown("### ✅ 3. What is the engagement ratio (AppOpens / RegisteredUsers) per device brand?")
    if 'AppOpens' in df.columns:
        ratio_df = df.groupby('Brand')[['RegisteredUsers', 'AppOpens']].sum()
        ratio_df = ratio_df[ratio_df['RegisteredUsers'] > 0]
        ratio_df['EngagementRatio'] = ratio_df['AppOpens'] / ratio_df['RegisteredUsers']
        top_ratio = ratio_df.sort_values('EngagementRatio', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=top_ratio['EngagementRatio'], y=top_ratio.index, palette='viridis', ax=ax)
        ax.set_xlabel("Engagement Ratio (AppOpens / RegisteredUsers)")
        ax.set_ylabel("Device Brand")
        ax.set_title("Top 10 Device Brands by Engagement Ratio")
        st.pyplot(fig)
    else:
        st.warning("⚠️ 'AppOpens' column not found. Skipping engagement ratio chart.")

    # ✅ 4. Trend Over Time
    st.markdown("### ✅ 4. How has the usage of top device brands changed over time?")
    top_brands = df.groupby('Brand')['RegisteredUsers'].sum().sort_values(ascending=False).head(5).index
    trend_df = df[df['Brand'].isin(top_brands)]
    trend_grouped = trend_df.groupby(['YearQuarter', 'Brand'])['RegisteredUsers'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=trend_grouped, x='YearQuarter', y='RegisteredUsers', hue='Brand', marker='o', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_xlabel("Year-Quarter")
    ax.set_ylabel("Registered Users")
    ax.set_title("Registered Users Trend Over Time by Top 5 Device Brands")
    st.pyplot(fig)

    # ✅ 5. Heatmap by Region
    st.markdown("### ✅ 5. Is there any correlation between device brand and region-wise performance?")
    heatmap_df = df.groupby(['State', 'Brand'])['RegisteredUsers'].sum().unstack().fillna(0)
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(heatmap_df, cmap='YlGnBu', linewidths=0.5, linecolor='grey', ax=ax)
    ax.set_title("Device Brand vs State: Registered Users Heatmap")
    ax.set_xlabel("Device Brand")
    ax.set_ylabel("State")
    st.pyplot(fig)

    st.success("📊 All 5 device engagement questions visualized successfully.")
