import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🛒 Customer Behavior Analysis Dashboard")

# Load data
df = pd.read_csv("customer_shopping_behavior.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# Revenue by Category
st.subheader("Revenue by Category")
fig, ax = plt.subplots()
sns.barplot(x="Category", y="Purchase Amount (USD)", data=df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Gender distribution
st.subheader("Customer Distribution by Gender")
st.bar_chart(df["Gender"].value_counts())

# Age distribution
st.subheader("Age Distribution")
st.hist(df["Age"])

st.success("Dashboard Loaded Successfully 🚀")