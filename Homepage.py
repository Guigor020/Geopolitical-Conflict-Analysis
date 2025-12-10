import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Analyse des Fatalités", 
    layout="wide",
    page_icon="📊"
)

# Title and introduction
st.title("📊 Analyse des Fatalités - Conflit ISR/PSE")
st.markdown("""
    Bienvenue sur l'application d'analyse des données de fatalités. 
    Utilisez le menu à gauche pour explorer les différentes analyses disponibles.
""")

# Sidebar for navigation
with st.sidebar:
    st.header("Menu de Navigation")
    st.markdown("""
        - **📈 Analyse des tendances** : Explorez les tendances des fatalités au fil du temps.
        - **👥 Analyse démographique** : Examinez les caractéristiques des victimes.
        - **🌍 Analyse géospatiale** : Visualisez la répartition des décès sur une carte et identifiez les zones qui ont connu des niveaux de violence plus élevés.
        - **📈 Analyse des victimes** : Identifiez les caractéristiques communes entre les victimes.
        - **📈 Analyse des armes utilisées** : Déterminez les armes ou méthodes les plus fréquemment utilisées et évaluez leur impact.
    """)
    st.markdown("---")
    st.markdown("ℹ️ Pour plus d'informations, contactez-nous.")

# Image or graph for introduction
st.image(
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yS57wW4sprpEgtzDMuLmfAHaE8%26pid%3DApi&f=1&ipt=4bf01b2902d96e27a579cc8d62cac20dbda6b410e4793e235fb45c2d0ab36829&ipo=images", 
    use_container_width=True,
    caption="Visualisation des données de fatalités"
)

# section for key insights
st.subheader("🔍 Principales Insights")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total des Fatalités", "11,124")
with col2:
    st.metric("Moyenne Mensuelle", "41.66")
with col3:
    st.metric("Période la plus Critique", "2014", "+ de 1600 fatalités")


# footer
st.markdown("---")
st.markdown("© 2025 - Tous droits réservés. Développé par [Mouhamadou Gorgui CISSE](#).")