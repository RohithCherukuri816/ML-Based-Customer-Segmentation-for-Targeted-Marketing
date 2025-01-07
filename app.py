import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the customer data
data = pd.read_csv('customer_data_with_clusters.csv')  # Replace with your dataset
clusters = data['Cluster']  # Assuming cluster labels exist

# Streamlit dashboard layout
st.title("Customer Segmentation Dashboard")
st.sidebar.header("Options")

# Cluster visualization
st.header("Cluster Distribution")
fig, ax = plt.subplots()
sns.countplot(x=clusters, ax=ax)
st.pyplot(fig)

# Cluster-specific analysis
st.header("Cluster Details")
cluster_selected = st.selectbox("Select Cluster", sorted(data['Cluster'].unique()))
st.write(data[data['Cluster'] == cluster_selected].describe())

# Feature visualization
st.header("Feature Analysis")
feature = st.selectbox(
    "Select Feature", 
    ['Age', 'Gender_Encoded', 'Spending_Score_Encoded', 'Family_Size', 'Ever_Married_Encoded']
)
fig, ax = plt.subplots()
sns.boxplot(x='Cluster', y=feature, data=data, ax=ax)
st.pyplot(fig)
