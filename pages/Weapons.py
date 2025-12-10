import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Sidebar for navigation
with st.sidebar:
    st.header("Menu de Navigation")
    st.markdown("""
        - **📈 Analyse des armes utilisées** : Déterminez les armes ou méthodes les plus fréquemment utilisées et évaluez leur impact.
    """)
    st.markdown("---")
    st.markdown("ℹ️ Pour plus d'informations, contactez-nous.")

# Title of the page
st.title("Analysis of Weapons Used in Fatalities")

# Load the dataset
file_path = "fatalities_isr_pse_conflict_2000_to_2023.csv"
data = pd.read_csv(file_path)


# Count frequency of weapons or methods used
ammunition_counts = data['ammunition'].value_counts()

# Display the most frequently used weapons
st.subheader("Most Frequently Used Weapons")
top_weapons = ammunition_counts.head(10)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_weapons.values, y=top_weapons.index, palette="Blues_r", ax=ax)
ax.set_title("Top 10 Weapons/Methods Used")
ax.set_xlabel("Number of Fatalities")
ax.set_ylabel("Weapon/Method")
st.pyplot(fig)

# Optional: Analyze weapon usage over time
st.subheader("Trend of Weapon Usage Over Time")
data['date_of_event'] = pd.to_datetime(data['date_of_event'], errors='coerce')
weapon_trend = data.groupby([data['date_of_event'].dt.to_period('Y'), 'ammunition']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(12, 6))
weapon_trend[top_weapons.index].plot(ax=ax, cmap="tab20", linewidth=2)
ax.set_title("Yearly Trend of Weapon Usage (Top 10)")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Fatalities")
st.pyplot(fig)
