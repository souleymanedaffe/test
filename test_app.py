import streamlit as st
import pandas as pd

st.title("Test de chargement Streamlit")
st.write("✅ L'application Streamlit fonctionne bien.")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Retail.csv", nrows=1000)
        st.success("Fichier CSV chargé avec succès !")
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement du CSV : {e}")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.write("Aperçu des données :")
    st.dataframe(df.head())
else:
    st.warning("Le fichier est vide ou introuvable.")
