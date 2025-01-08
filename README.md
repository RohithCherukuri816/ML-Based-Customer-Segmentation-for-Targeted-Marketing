# **ML-Based-Customer-Segmentation-for-Targeted-Marketing**

This repository contains a **Customer Segmentation** project that leverages **Machine Learning (ML)** techniques to analyze customer data, group them into distinct segments, and provide valuable insights for marketing and sales strategies. The project utilizes clustering algorithms, model evaluation metrics, and visualization techniques to generate actionable insights.

---

## **Table of Contents**

- [Overview](#overview)
- [Technologies](#technologies)
- [Dataset Description](#dataset-description)
- [Features](#features)
- [Model Evaluation](#model-evaluation)
- [Dashboard](#dashboard)
- [Analytics](#Analytics)
- [Key Links](#Key-Links)

---

## **Overview**

The goal of this project is to apply **unsupervised learning** to segment customers based on key features, which can be used for targeted marketing, product recommendations, and customer retention strategies. The project employs the **K-Means clustering algorithm** for customer segmentation, followed by model evaluation and a real-time interactive dashboard.
The project highlights:
- Preprocessing and handling missing data.
- Machine learning clustering with K-Means.
- A Streamlit dashboard for visualizing insights.
- Evaluation metrics to validate the clustering model.

---

## **Technology Stack**

- **Python 3.x**
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib** / **Seaborn** – Data visualization
- **Scikit-learn** – Machine Learning algorithms and tools
- **Streamlit** – Interactive Dashboard
- **Flask** – Web framework for the recommendation system
- **ngrok** – Expose local server to the internet for public access
- **Google Colab** – For experiments and quick testing

---

## **Dataset Description**

The dataset used in this project contains:

### **Demographics Details:**
- Age
- Ever Married
- Graduated
- Profession
- Family size, etc.<br>

### **Behavioral details:**
- Spending Score
-  Work experience, etc.

The data is preprocessed to handle missing values, scale numerical features, and encode categorical variables.

---

## **Features**

## 1. **Clustering**
- Use K-Means Clustering to segment customers.
- Visualize clusters using scatter plots and heatmaps.
 
## **2. Model Evaluation**

Evaluate clustering models with:
- Silhouette Score
- Calinski-Harabasz Index
- Davies-Bouldin Index

## **3. Dashboard**

A user-friendly Streamlit dashboard for:
- Visualizing customer segments.
- Exploring cluster distributions.

## **4. Analytics**

To enhance the analytical capabilities of this project, I integrated **Mixpanel**, a powerful analytics platform for tracking user behavior and customer profiles.

### **Steps for Mixpanel Integration**
1. **Customer Profiles**:
   - Pushed key customer attributes (e.g., age, profession, spending score, family size) to Mixpanel.
   - Each customer profile helps analyze demographic trends and behavioral insights.

2. **Event Tracking**:
   - Logged user interactions, such as segmentation checks and behavioral actions.
   - Events include:
     - `Segmentation Check`
     - `User Login`

3. **Mixpanel Dashboard**:
   - Used Mixpanel's [**Events**](https://github.com/RohithCherukuri816/RohithCherukuri816-ML-Based-Customer-Segmentation-for-Targeted-Marketing/blob/main/Events.png), [**Session Metrics**](https://github.com/RohithCherukuri816/RohithCherukuri816-ML-Based-Customer-Segmentation-for-Targeted-Marketing/blob/main/Session%20Metrics.png) to verify data uploads.
   - Analyzed retention, engagement, and [**User**](https://github.com/RohithCherukuri816/RohithCherukuri816-ML-Based-Customer-Segmentation-for-Targeted-Marketing/blob/main/Users.png) journeys.

---

## **Model Evaluation**
Here are the metrics used to evaluate the quality of clusters:
- Silhouette Score: Measures the cohesion of clusters.
- Davies-Bouldin Index: Compares the compactness and separation of clusters.
- Calinski-Harabasz Index: Assesses the ratio of within-cluster dispersion to between-cluster dispersion.

Check the results in the [Notebook](https://github.com/RohithCherukuri816/RohithCherukuri816-ML-Based-Customer-Segmentation-for-Targeted-Marketing/blob/main/ML_Based_Customer_Segmentation_for_Targeted_Marketing.ipynb).

---

## **Key Links**
[Notebook](https://github.com/RohithCherukuri816/RohithCherukuri816-ML-Based-Customer-Segmentation-for-Targeted-Marketing/blob/main/ML_Based_Customer_Segmentation_for_Targeted_Marketing.ipynb) – Detailed implementation and insights.

[Dataset](https://github.com/RohithCherukuri816/RohithCherukuri816-ML-Based-Customer-Segmentation-for-Targeted-Marketing/blob/main/customer_data.csv) – Customer data used for clustering.

[Deployment Link](https://ml-based-customer-segmentation-for-targeted-marketing.streamlit.app/) – Project is Live at here






   







