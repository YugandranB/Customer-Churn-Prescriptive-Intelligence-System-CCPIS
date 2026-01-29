# Customer Churn Prescriptive Intelligence System (CCPIS)

> An end-to-end customer analytics platform that predicts churn risk and generates AI-driven retention strategies using behavioral modeling and prescriptive intelligence.

CCPIS goes beyond traditional churn prediction by learning **customer purchase rhythm (Inter-Purchase Time)** and combining machine learning with **Generative AI reasoning** to deliver actionable, business-ready insights.

---

## 📌 Problem Statement

Most churn systems rely on static thresholds (example: no purchase in 90 days = churn).  
This leads to:

- False churn detection  
- Unnecessary discount campaigns  
- Revenue leakage  
- Poor customer experience  

CCPIS solves this by introducing **behavior-aware churn modeling** and **AI-powered prescriptive decision support**.

---

## 🧠 System Capabilities

- Behavioral churn prediction using XGBoost  
- Inter-Purchase Time (IPT) rhythm modeling  
- Leakage-safe model training strategy  
- Class imbalance handling with SMOTE  
- Customer segmentation using KMeans  
- AI-powered prescriptive recommendations (Gemini API)  
- Interactive analytics dashboard (Gradio)  
- Visual behavioral mapping of high-risk customers  

---

## 🏗 System Architecture











---

## 📊 Model Performance

- Validation ROC-AUC Score: 0.72  
- Training Methodology: Leakage-free modeling (Recency excluded)  
- Optimization Techniques:
  - SMOTE oversampling  
  - Log transformation on skewed variables  

### Why 0.72 Is Strong

Customer churn prediction is a real-world noisy problem.  
A 0.72 ROC-AUC provides reliable customer risk ranking, which is highly valuable for business prioritization and marketing strategy optimization.

---

## 💡 Key Innovation — Inter-Purchase Time (IPT)

Unlike traditional churn models, CCPIS models individual customer buying rhythm.

Example:

| Customer Type | Purchase Cycle | Risk Interpretation |
---------------|----------------|---------------------
Frequent Buyer | Every 10 days  | At risk at 20 days  
Seasonal Buyer | Every 100 days | Still safe at 90 days  

This significantly reduces false churn labeling.

---

## 🤖 Prescriptive Intelligence Layer

The AI engine analyzes:

- Customer churn probability  
- Behavioral segment  
- Purchase history  
- Product affinity  
- Geographic context  

And generates:

- Retention strategy recommendations  
- Campaign messaging ideas  
- Discount vs engagement decision guidance  
- Psychological churn drivers  

This converts analytics into actionable business decisions.

---

## 🖥 Decision Intelligence Dashboard

The Gradio dashboard provides:

- Live churn risk telemetry  
- Behavioral segmentation view  
- Visual customer positioning map  
- AI-generated marketing playbooks  
- VIP customer auditing  

Designed as an internal CRM analytics command center.

---

## 🛠 Tech Stack

| Layer | Technology |
------|---------
Language | Python  
Data Processing | Pandas, NumPy  
Modeling | XGBoost, Scikit-learn  
Imbalance Handling | SMOTE  
Clustering | KMeans  
Visualization | Matplotlib  
AI Reasoning | Google Gemini API  
UI Layer | Gradio  

---

## 📂 Project Structure



