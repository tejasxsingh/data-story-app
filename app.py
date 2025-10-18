
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Interactive Data Story", layout="wide")

st.title("Global Internet Growth")
st.write("Explore how internet usage has changed across regions over time.")

# Load the CSV data
data = pd.read_csv("data/internet_usage.csv")

region = st.selectbox("Select a region:", sorted(data["Region"].unique()))
filtered = data[data["Region"] == region]

chart = (
    alt.Chart(filtered)
    .mark_line(point=True)
    .encode(
        x="Year:O",
        y="Internet Users (%):Q",
        color=alt.value("#0073e6")
    )
)

st.altair_chart(chart, use_container_width=True)

st.markdown("""
**About this project:**  
A Python + Streamlit app that shows how data can tell stories through interactive visuals.
""")
