# https://docs.streamlit.io/develop/api-reference

import os
import streamlit as st
import pandas as pd
import logging

# --------- settings --------------

logging.basicConfig(level=logging.INFO)

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "vgsales.csv")


# --------- pandas --------------

df = pd.read_csv(csv_path)

df["Year"] = df["Year"].dropna()
df["Publisher"] = df["Publisher"].fillna("Anonymous")

platform_options = ["All"] + list(df["Platform"].dropna().unique())
genre_options = ["All"] + list(df["Genre"].dropna().unique())
publisher_options = ["All"] + list(df["Publisher"].dropna().unique())

# --------- streamlit --------------

st.title("10 yrs ago Game stuff")

option_Platform = st.selectbox("Platform", platform_options)
option_Genre = st.selectbox("Genre", genre_options)
option_Publisher = st.selectbox("Publisher", publisher_options)

filters = {
    "Platform": option_Platform,
    "Genre": option_Genre,
    "Publisher": option_Publisher
}


def apply_filter(df):
    final = df.copy()
    for col, option in filters.items():
        if option != "All":
            final = final[final[col] == option]
    return final


show = apply_filter(df)
yearly = show.groupby("Year", as_index=False)[["Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()

st.line_chart(yearly, x="Year", y=["Global_Sales","NA_Sales","EU_Sales","JP_Sales","Other_Sales"], y_label="Total Sales (in Millions)")
st.dataframe(show)