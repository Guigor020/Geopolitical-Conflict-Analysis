import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Title of the page
st.title("Victim Profiles Analysis")

# Load the dataset
file_path = "C:/Users/USER/Documents/Mundiapolis/M1/projets/M1/Project_python/fatalities_isr_pse_conflict_2000_to_2023.csv"
data = pd.read_csv(file_path)

# Sidebar for navigation
with st.sidebar:
    st.header("Menu de Navigation")
    st.markdown("""
        - **📈 Analyse des victimes** : Identifiez les caractéristiques communes entre les victimes.
    """)
    st.markdown("---")
    st.markdown("ℹ️ Pour plus d'informations, contactez-nous.")

# Inspect columns related to victim demographics
st.sidebar.header("Filter Demographics")
age_column = 'age'  # Replace with actual column name for age
gender_column = 'gender'  # Replace with actual column name for gender
citizenship_column = 'citizenship'  # Replace with actual column name for citizenship
residence_column = 'place_of_residence'  # Replace with actual column name for place of residence

# Sidebar filters
age_filter = st.sidebar.slider("Select Age Range", 
                               int(data[age_column].min()), 
                               int(data[age_column].max()), 
                               (int(data[age_column].min()), int(data[age_column].max())))
data = data[(data[age_column] >= age_filter[0]) & (data[age_column] <= age_filter[1])]


selected_genders = st.sidebar.multiselect("Select Gender", data[gender_column].unique(), data[gender_column].unique())
data = data[data[gender_column].isin(selected_genders)]


selected_citizenships = st.sidebar.multiselect("Select Citizenship", data[citizenship_column].unique(), data[citizenship_column].unique())
data = data[data[citizenship_column].isin(selected_citizenships)]


selected_residences = st.sidebar.multiselect("Select Place of Residence", data[residence_column].unique(), data[residence_column].unique())
data = data[data[residence_column].isin(selected_residences)]

# Analysis: Gender distribution
st.subheader("Gender Distribution")
gender_counts = data[gender_column].value_counts()
fig, ax = plt.subplots()
gender_counts.plot(kind='bar', color=['#007acc', '#ff9999'], ax=ax)
ax.set_title("Gender Distribution")
ax.set_ylabel("Number of Victims")
ax.set_xlabel("Gender")
st.pyplot(fig)

# Analysis: Age distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(data[age_column], bins=20, kde=True, color='blue', ax=ax)
ax.set_title("Age Distribution of Victims")
ax.set_xlabel("Age")
ax.set_ylabel("Count")
st.pyplot(fig)

# Analysis: Citizenship
# Group smaller categories into "Other"
threshold = 0.01  # 1% threshold for grouping
citizenship_counts = data[citizenship_column].value_counts(normalize=True)
major_citizenships = citizenship_counts[citizenship_counts >= threshold]
other_citizenships = citizenship_counts[citizenship_counts < threshold].sum()
# Combine major categories with "Other"
combined_counts = pd.concat([major_citizenships, pd.Series({"Other": other_citizenships})])
combined_counts = combined_counts * 100  # Convert to percentages
# Plot the updated pie chart
fig, ax = plt.subplots()
combined_counts.plot(
    kind='pie',
    autopct='%1.2f%%',
    startangle=45,
    ax=ax,
    colors=plt.cm.Paired.colors
)
ax.set_title("Citizenship Distribution (Grouped)")
ax.set_ylabel("")  # Hide y-axis label for pie chart
st.pyplot(fig)


# Analysis: Place of Residence
st.subheader("Place of Residence Distribution")
residence_counts = data[residence_column].value_counts().head(10)
fig, ax = plt.subplots()
residence_counts.plot(kind='barh', color='green', ax=ax)
ax.set_title("Top 10 Places of Residence")
ax.set_xlabel("Number of Victims")
ax.set_ylabel("Place of Residence")
st.pyplot(fig)
