import streamlit as st
import pandas as pd

st.set_page_config(page_title="Test Analyse Ventes", layout="wide")
st.title("📊 Analyse de ventes — Test léger")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("vente_sample.csv")
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
        df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
        df['MonthPeriod'] = df['InvoiceDate'].dt.to_period("M")
        return df
    except Exception as e:
        st.error(f"Erreur de chargement : {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("⚠️ Aucune donnée disponible.")
else:
    st.success(f"✅ {len(df)} lignes chargées depuis vente_sample.csv")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("💰 Top Clients par Total d'achat")
    top_clients = (
        df.groupby("CustomerID")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(5)
    )
    st.dataframe(top_clients)

    st.subheader("📦 Quantités vendues par produit")
    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(5)
    )
    st.dataframe(top_products)
