import streamlit as st
import plotly.express as px
import pandas as pd

# Seiteneinstellungen
st.set_page_config(page_title="Meine Data Science Visitenkarte", layout="wide")

# Header / Profil
st.title("Hallo, ich bin [Dein Name] 👋")
st.subheader("Data Scientist & KI-Entwickler")

# Layout aufteilen (2 Spalten)
col1, col2 = st.columns([1, 2])

with col1:
    st.image("dein_profilbild.jpg", width=200)
    st.markdown("[Mein Kaggle-Profil](https://kaggle.com) 🚀")
    st.markdown("[Mein GitHub-Profil](https://github.com) 💻")

with col2:
    st.write("Hier steht deine kurze, packende Biografie. Erzähle, welche Probleme du am liebsten mit Daten löst.")
    
    # Interaktives Skill-Diagramm
    st.write("### Meine Tech-Skills")
    skills_data = pd.DataFrame({
        "Skill": ["Python", "Machine Learning", "SQL", "Data Visualisation", "Streamlit"],
        "Level": [90, 80, 85, 75, 90]
    })
    fig = px.bar(skills_data, x="Level", y="Skill", orientation="h", color="Level", text="Level")
    st.plotly_chart(fig, use_container_width=True)
