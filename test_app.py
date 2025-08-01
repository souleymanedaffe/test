import streamlit as st
import pandas as pd

st.set_page_config(page_title="Test App", layout="wide")
st.title("🚀 Test Streamlit : Chargement des données")

# ✅ Ligne de confirmation que le script démarre
st.write("🔄 Initialisation de l'application...")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("vente_sample.csv")
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
        df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
        df['MonthPeriod'] = df['InvoiceDate'].dt.to_period("M")
        return df
    except FileNotFoundError:
        st.error("❌ Fichier vente_sample.csv introuvable.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement : {e}")
        return pd.DataFrame()

# 📊 Chargement
df = load_data()

if df.empty:
    st.warning("⚠️ Le fichier est vide ou invalide.")
else:
    st.success(f"✅ {len(df)} lignes chargées.")
    st.dataframe(df.head())

    # Petite analyse rapide
    st.subheader("📦 Top 5 Produits")
    top_produits = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(5)
    )
    st.dataframe(top_produits)

    st.subheader("👥 Top 5 Clients")
    top_clients = (
        df.groupby("CustomerID")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(5)
    )
    st.dataframe(top_clients)
