import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Title of the page
st.title("Geospatial Analysis of Fatalities")

# Load the dataset
file_path = "C:/Users/USER/Documents/Mundiapolis/M1/projets/M1/Project_python/fatalities_isr_pse_conflict_2000_to_2023.csv"
data = pd.read_csv(file_path)

# Sidebar for navigation
with st.sidebar:
    st.header("Menu de Navigation")
    st.markdown("""
        - **🌍 Analyse géospatiale** : Visualisez la répartition des décès sur une carte et identifiez les zones qui ont connu des niveaux de violence plus élevés.
    """)
    st.markdown("---")
    st.markdown("ℹ️ Pour plus d'informations, contactez-nous.")

# Sidebar filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect(
    "Select Regions", options=data['event_location_region'].unique(), default=data['event_location_region'].unique()
)
selected_district = st.sidebar.multiselect(
    "Select Districts", options=data['event_location_district'].unique(), default=data['event_location_district'].unique()
)

# Filter data
filtered_data = data[
    (data['event_location_region'].isin(selected_region)) & 
    (data['event_location_district'].isin(selected_district))
]

# Display summary
st.write(f"Total Fatalities: {len(filtered_data)} events displayed.")

# Visualize fatalities by region
region_counts = filtered_data['event_location_region'].value_counts()

st.subheader("Fatalities by Region")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=region_counts.index, y=region_counts.values, palette="viridis", ax=ax)
ax.set_title("Number of Fatalities by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Number of Fatalities")
st.pyplot(fig)

# Prepare data for mapping
@st.cache_data
def geocode_locations(data):
    """Exemples de latitude - longitude"""
    locations = {
        "Gaza": [31.5, 34.47],
        "West Bank": [31.95, 35.25],
        "Israel": [32.1, 34.8]
    }
    data['lat'] = data['event_location_region'].map(lambda x: locations.get(x, [0, 0])[0])
    data['lon'] = data['event_location_region'].map(lambda x: locations.get(x, [0, 0])[1])
    return data

mapped_data = geocode_locations(filtered_data)

# Create interactive map
st.subheader("Interactive Map of Fatalities")
m = folium.Map(location=[31.5, 35.0], zoom_start=7)

# Add heatmap
heat_data = mapped_data[['lat', 'lon']].dropna().values.tolist()
HeatMap(heat_data).add_to(m)

# Display map
st_folium(m, width=700, height=500)
