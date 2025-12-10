import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from datetime import datetime

# Set a visually appealing theme
sns.set_theme(style="whitegrid")

# Load the dataset
file_path = "C:/Users/USER/Documents/Mundiapolis/M1/projets/M1/Project_python/fatalities_isr_pse_conflict_2000_to_2023.csv"
data = pd.read_csv(file_path)

# Title and introduction
st.title("Fatalities Trends Over Time (2000-2023)")
st.write("This visualization shows the monthly trends in fatalities over time, with options to analyze significant changes.")

# Sidebar for navigation
with st.sidebar:
    st.header("Menu de Navigation")
    st.markdown("""
        - **📈 Analyse des tendances** : Explorez les tendances des fatalités au fil du temps.
    """)
    st.markdown("---")
    st.markdown("ℹ️ Pour plus d'informations, contactez-nous.")
# Data Preprocessing
data['date_of_event'] = pd.to_datetime(data['date_of_event'], errors='coerce')
data['year_month'] = data['date_of_event'].dt.to_period('M')

# Count fatalities per month
monthly_trends = data.groupby('year_month').size()

# Streamlit Interface
st.subheader("Monthly Fatalities Trend (2000-2023)")

# Matplotlib Plot in Streamlit with enhanced visuals
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=monthly_trends.index.astype(str), y=monthly_trends.values, color='red', linewidth=2.5, marker='o', markersize=8, ax=ax)
ax.set_title('Monthly Fatalities Trend (2000-2023)', fontsize=18, pad=20)
ax.set_xlabel('Year-Month', fontsize=14)
ax.set_ylabel('Number of Fatalities', fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.grid(axis='x', linestyle='--', alpha=0.7)
plt.xticks(np.arange(0, len(monthly_trends), step=24), rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
st.pyplot(fig)

# Add a widget to analyze significant changes
st.subheader("Analyze Significant Changes")
threshold = st.slider(
    "Select the threshold for significant changes (number of fatalities):",
    min_value=10,
    max_value=1750,
    value=200,
    step=10,
    help="Adjust the slider to define what constitutes a significant change in fatalities."
)

# Identify significant spikes or declines
significant_changes = monthly_trends.diff().abs() > threshold
significant_years = monthly_trends.index[significant_changes]

# Display significant changes with enhanced visuals
if len(significant_years) > 0:
    st.write(f"**Years with significant changes (greater than {threshold} fatalities):**")
    for year in significant_years:
        st.markdown(f"- **{year}**: {monthly_trends[year]} fatalities")
else:
    st.write("**No significant changes found based on the selected threshold.**")

# Add a section for additional insights
st.subheader("Additional Insights")
st.write("Explore the data further to uncover patterns or trends in specific time periods.")

# Add a date range filter for interactive analysis
st.write("### Filter by Date Range")
start_date = st.date_input("Start Date", datetime(2000, 1, 1))
end_date = st.date_input("End Date", datetime(2023, 12, 31))

# Filter data based on selected date range
filtered_data = data[(data['date_of_event'] >= pd.to_datetime(start_date)) & (data['date_of_event'] <= pd.to_datetime(end_date))]
filtered_monthly_trends = filtered_data.groupby('year_month').size()

# Display filtered trends
st.write(f"**Monthly Fatalities Trend ({start_date} to {end_date}):**")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(x=filtered_monthly_trends.index.astype(str), y=filtered_monthly_trends.values, color='blue', linewidth=2.5, marker='o', markersize=8, ax=ax2)
ax2.set_title(f'Monthly Fatalities Trend ({start_date} to {end_date})', fontsize=18, pad=20)
ax2.set_xlabel('Year-Month', fontsize=14)
ax2.set_ylabel('Number of Fatalities', fontsize=14)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='x', linestyle='--', alpha=0.7)
plt.xticks(np.arange(0, len(filtered_monthly_trends), step=12), rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
st.pyplot(fig2)

# Add a summary of the filtered data
st.write("### Summary of Filtered Data")
st.write(f"**Total Fatalities in the Selected Date Range:** {filtered_monthly_trends.sum()}")
st.write(f"**Average Monthly Fatalities:** {filtered_monthly_trends.mean():.2f}")
st.write(f"**Maximum Monthly Fatalities:** {filtered_monthly_trends.max()} (occurred in {filtered_monthly_trends.idxmax()})")
st.write(f"**Minimum Monthly Fatalities:** {filtered_monthly_trends.min()} (occurred in {filtered_monthly_trends.idxmin()})")

# Add a footer
st.write("---")
st.write("**Data Source:** [KAGGLE]")