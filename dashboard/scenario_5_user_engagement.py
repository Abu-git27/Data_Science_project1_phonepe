import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.subheader(" Scenario 5: User Engagement Analysis (District Level)")

    sns.set(style="whitegrid")
    try:
        map_df = pd.read_csv('map_user.csv')
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return

    map_df = map_df[map_df['District'].str.lower() != 'unknown']
    map_df = map_df[map_df['RegisteredUsers'] > 0]
    map_df['EngagementRatio'] = map_df['AppOpens'] / map_df['RegisteredUsers']

    # Chart 1: Top 10 Districts by Registered Users
    st.markdown("### 1.Top 10 Districts by Registered Users")
    top_users = map_df.groupby('District')['RegisteredUsers'].sum().sort_values(ascending=False).head(10)

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_users.values, y=top_users.index, palette='viridis', ax=ax1)
    ax1.set_title('Top 10 Districts by Registered Users')
    ax1.set_xlabel('Registered Users')
    ax1.set_ylabel('District')
    st.pyplot(fig1)

    # Chart 2: Top 10 Districts by App Opens
    st.markdown("###  2.Top 10 Districts by App Opens")
    top_opens = map_df.groupby('District')['AppOpens'].sum().sort_values(ascending=False).head(10)

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_opens.values, y=top_opens.index, palette='rocket', ax=ax2)
    ax2.set_title('Top 10 Districts by App Opens')
    ax2.set_xlabel('App Opens')
    ax2.set_ylabel('District')
    st.pyplot(fig2)

    # Chart 3: Engagement Pattern (with legend)
    st.markdown("### 3.Engagement Pattern: App Opens vs Registered Users")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    scatter = sns.scatterplot(data=map_df, x='RegisteredUsers', y='AppOpens', hue='State', alpha=0.7, ax=ax3)
    ax3.set_title('App Opens vs Registered Users')
    ax3.set_xlabel('Registered Users')
    ax3.set_ylabel('App Opens')
    ax3.grid(True)
    ax3.legend(loc='best', bbox_to_anchor=(1, 1))
    st.pyplot(fig3)

    # Chart 4: State-wise Spread of Engagement Ratio (rotated axes)
    st.markdown("### 4.State-wise Spread of Engagement Ratio (Rotated Axes)")
    fig4, ax4 = plt.subplots(figsize=(10, 8))
    state_engage = map_df.groupby('State')['EngagementRatio'].mean().sort_values()
    sns.barplot(y=state_engage.index, x=state_engage.values, palette='coolwarm', ax=ax4)
    ax4.set_title('Average Engagement Ratio by State')
    ax4.set_xlabel('Engagement Ratio (App Opens / Registered Users)')
    ax4.set_ylabel('State')
    st.pyplot(fig4)

    # Chart 5: Top 10 Districts by Engagement Ratio
    st.markdown("### 5.Top 10 Districts by Engagement Ratio")
    top_ratio = map_df.groupby('District')['EngagementRatio'].mean().sort_values(ascending=False).head(10)

    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_ratio.values, y=top_ratio.index, palette='mako', ax=ax5)
    ax5.set_title('Top 10 Districts by Engagement Ratio')
    ax5.set_xlabel('Engagement Ratio')
    ax5.set_ylabel('District')
    st.pyplot(fig5)

    st.success(" All visualizations rendered successfully for User Engagement Analysis.")
