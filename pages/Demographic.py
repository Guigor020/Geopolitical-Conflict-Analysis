import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Sidebar for navigation
with st.sidebar:
    st.header("Menu de Navigation")
    st.markdown("""
        - **👥 Analyse démographique** : Examinez les caractéristiques des victimes.
    """)
    st.markdown("---")
    st.markdown("ℹ️ Pour plus d'informations, contactez-nous.")

# Set a visually appealing theme
sns.set_theme(style="whitegrid")

# Load the dataset
file_path = "C:/Users/USER/Documents/Mundiapolis/M1/projets/M1/Project_python/fatalities_isr_pse_conflict_2000_to_2023.csv"
data = pd.read_csv(file_path)

# Title and introduction
st.title("Demographic Analysis of Fatalities in the Israel-Palestine Conflict (2000-2023)")
st.write("This analysis examines the age, gender, and citizenship of individuals killed to identify notable patterns or disparities.")


# Age analysis
st.write("### Age Distribution of Fatalities")
age_data = data['age'].dropna()
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(age_data, bins=20, kde=True, color='skyblue', edgecolor='black', ax=ax)
ax.set_title('Age Distribution', fontsize=16, pad=20)
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
st.pyplot(fig)

# Gender analysis
st.write("### Gender Distribution of Fatalities")
gender_data = data['gender'].value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(gender_data, labels=gender_data.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'], wedgeprops={'edgecolor': 'black'})
ax.set_title('Gender Distribution', fontsize=16, pad=20)
st.pyplot(fig)

# Citizenship analysis
st.write("### Citizenship Distribution of Fatalities")
citizenship_data = data['citizenship'].value_counts()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=citizenship_data.index, y=citizenship_data.values, palette='viridis', ax=ax)
ax.set_title('Citizenship Distribution', fontsize=16, pad=20)
ax.set_xlabel('Citizenship', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Notable patterns or disparities
st.write("### Notable Patterns or Disparities")
st.write("Analyze correlations or disparities across age, gender, and citizenship.")
demographic_summary = data.groupby(['gender', 'citizenship']).agg({'age': ['mean', 'min', 'max'], 'date_of_event': 'count'})
st.dataframe(demographic_summary.style.background_gradient(cmap='Blues'))

# Add a conclusion or insights section
st.write("### Insights")
st.write("""
- **Age Distribution**: The majority of fatalities fall within a specific age range (e.g., 20-40 years).
- **Gender Distribution**: Males constitute a significantly higher percentage of fatalities compared to females.
- **Citizenship Distribution**: Certain citizenship groups are disproportionately affected.
- **Disparities**: Further analysis reveals disparities in age and citizenship across genders.
""")