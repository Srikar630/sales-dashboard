"""Interactive sales dashboard built with Streamlit."""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")


@st.cache_data
def load():
    return pd.read_csv("sales.csv", parse_dates=["date"])


df = load()

# Sidebar filters
regions = st.sidebar.multiselect("Region", sorted(df.region.unique()), default=sorted(df.region.unique()))
products = st.sidebar.multiselect("Product", sorted(df["product"].unique()), default=sorted(df["product"].unique()))
filtered = df[df.region.isin(regions) & df["product"].isin(products)]

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Total revenue", f"${filtered.revenue.sum():,.0f}")
c2.metric("Units sold", f"{filtered.units.sum():,}")
c3.metric("Orders", f"{len(filtered):,}")

# Charts
st.subheader("Monthly revenue")
monthly = filtered.set_index("date").resample("MS").revenue.sum()
st.line_chart(monthly)

left, right = st.columns(2)
left.subheader("Revenue by product")
left.bar_chart(filtered.groupby("product").revenue.sum())
right.subheader("Revenue by region")
right.bar_chart(filtered.groupby("region").revenue.sum())

with st.expander("View raw data"):
    st.dataframe(filtered)
