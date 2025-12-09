import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")

# ------------------ LOAD DATA ------------------
df = pd.read_csv(
    r"C:\Users\lenovo\python learn\Project py\Full Cap Project\Dataset\WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# ------------------ DASHBOARD TITLE ------------------
st.title("📊 HR Attrition Dashboard")
st.markdown("Interactive dashboard similar to Power BI built using Streamlit.")
st.write("---")

# ------------------ SIDEBAR FILTERS ------------------
st.sidebar.header("🔎 Apply Filters")

department = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

jobrole = st.sidebar.multiselect(
    "Job Role",
    options=df["JobRole"].unique(),
    default=df["JobRole"].unique()
)

overtime = st.sidebar.multiselect(
    "Over Time",
    options=df["OverTime"].unique(),
    default=df["OverTime"].unique()
)

# ------------------ FILTER DATA ------------------
df_filtered = df[
    (df["Department"].isin(department)) &
    (df["JobRole"].isin(jobrole)) &
    (df["OverTime"].isin(overtime))
]

# ------------------ PREVIEW FILTERED DATA ------------------
st.subheader("📈 Filtered Dataset Preview")
st.dataframe(df_filtered.head())
st.write("---")

# ---------------------------------------------------------
#           📊 CLEAN & PROFESSIONAL DASHBOARD VISUALS
# ---------------------------------------------------------

st.header("📊 HR Insights Summary")

col1, col2 = st.columns(2)

# -------- Attrition Distribution --------
with col1:
    st.subheader("📌 Attrition Distribution")
    fig, ax = plt.subplots(figsize=(5,4))
    sns.countplot(data=df_filtered, x="Attrition", palette="Spectral", ax=ax)
    st.pyplot(fig)

# -------- Attrition by Job Role --------
with col2:
    st.subheader("📌 Attrition by Job Role")
    fig, ax = plt.subplots(figsize=(7,4))
    sns.countplot(data=df_filtered, x="JobRole", hue="Attrition", palette="coolwarm", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -------- Monthly Income Trend --------
st.subheader("📉 Monthly Income vs Age Trend")
fig, ax = plt.subplots(figsize=(10,4))
sns.lineplot(
    data=df_filtered.sort_values("Age"),
    x="Age",
    y="MonthlyIncome",
    color="purple",
    linewidth=2,
    ax=ax
)
st.pyplot(fig)

# -------- Correlation Heatmap --------
st.subheader("🔥 Correlation Heatmap (Numeric Features Only)")
numeric_df = df_filtered.select_dtypes(include='number')

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df.corr(), cmap="YlGnBu", linewidths=0.5, annot=False, ax=ax)
st.pyplot(fig)

# -------- Boxplot --------
st.subheader("📦 Monthly Income by Attrition")
fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(data=df_filtered, x="Attrition", y="MonthlyIncome", palette="Set2", ax=ax)
st.pyplot(fig)

st.write("---")
st.info("Dashboard loaded successfully. Use sidebar filters to explore HR Attrition patterns.")
