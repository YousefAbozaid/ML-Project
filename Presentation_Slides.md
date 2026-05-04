---
marp: true
theme: default
paginate: true
header: 'GenZ Social Media Behavior Analysis'
footer: 'Data Science & Machine Learning Final Project'
style: |
  section {
    font-size: 1.25rem;
  }
  h1 {
    color: #2C3E50;
  }
  h2 {
    color: #34495E;
    border-bottom: 2px solid #3498DB;
    padding-bottom: 5px;
  }
  blockquote {
    background: #F8F9FA;
    border-left: 5px solid #3498DB;
    padding: 10px;
    font-style: italic;
  }
---

<!-- _class: lead -->

# Predicting Nighttime Social Media Usage among GenZ
### An In-Depth Exploratory Analysis and Logistic Regression Project

**Dataset Size:** 1,000,500 User Records
**Model Accuracy:** ~60%
**Presenter:** [Your Name / Group]

---

## 1. Executive Summary & Project Objectives

The primary objective of this project is to analyze the social media habits of Generation Z, specifically focusing on what drives late-night usage (`night_usage`). 

**Key Goals:**
- **Data Engineering:** Clean and preprocess a massive dataset containing over 1 million records.
- **Exploratory Data Analysis (EDA):** Uncover demographic and behavioral trends using visual data distributions.
- **Predictive Modeling:** Engineer features and deploy a Logistic Regression model to classify user nighttime habits based on their daily engagement and addiction levels.

---

## 2. Dataset Overview & Data Cleaning

We utilized the `genz_social_media_unclean.csv` dataset, initially featuring 1,000,500 rows and 13 variables.

**Cleaning Operations Performed:**
- **Feature Reduction:** Dropped `irrelevant_id` due to zero predictive power.
- **Handling Missing Values:**
  - `age`: 50,025 missing values. Replaced with the **Median** to prevent outlier skewing.
  - `primary_platform`: 30,015 missing values. Replaced with the **Mode** (most frequent).
- **Validation:** Ensured a strictly 0-null dataset post-cleaning.

---

## 3. Demographics Analysis

Understanding the core user base is crucial before modeling. The dataset reflects a predominantly young audience.

- **Average Age:** The mean age in the dataset is approximately 20 years old.

> *Insert your Gender Countplot (`sns.countplot(x=df['gender'])`) here:*
![Gender Distribution](insert_gender_countplot.png)

> *Insert your Age Histogram (`plt.hist(df['age'])`) here:*
![Age Histogram](insert_age_histogram.png)

---

## 4. Behavioral Analysis: Addiction Levels

We categorized users based on their perceived social media `addiction_level`. The breakdown highlights a significant portion of users falling into the "Medium" category.

**Class Distribution:**
- **Medium:** ~59.01% (590,135 users)
- **Low:** ~25.13% (251,345 users)
- **High:** ~15.90% (159,020 users)

> *Insert your Addiction Level Pie Chart (`plt.pie(count_class)`) here:*
![Addiction Level Distribution](insert_addiction_pie_chart.png)

---

## 5. Feature Engineering & Selection

To optimize our Logistic Regression model, we focused strictly on the most influential variables determined through correlation metrics and categorical graphing.

**Selected Predictive Features:**
1. `daily_usage_hours` (Numerical)
2. `avg_session_minutes` (Numerical)
3. `gender` (Categorical)
4. `addiction_level` (Categorical)

**Target Variable:** `night_usage` (Binary Output: 0 or 1)

---

## 6. Correlation Insights: What drives Night Usage?

Our exploratory graphs directly informed our feature selection, showing clear dependencies between categorical variables and late-night usage.

> *Insert your Night Usage by Gender Plot (`sns.countplot(x='gender', hue='night_usage')`) here:*
![Night Usage by Gender](insert_night_usage_gender.png)

> *Insert your Night Usage by Addiction Level Plot (`sns.countplot(x='addiction_level', hue='night_usage')`) here:*
![Night Usage by Addiction Level](insert_night_usage_addiction.png)

---

## 7. Data Encoding Strategies

Machine learning models require numerical input. We mapped our categorical text columns into integers using **Label Encoding**.

**Encoding Schema:**
- **Gender:** 
  - `Male` $\rightarrow$ 0
  - `Female` $\rightarrow$ 1
  - `Other` $\rightarrow$ 2
- **Addiction Level:** 
  - `Low` $\rightarrow$ 0
  - `Medium` $\rightarrow$ 1
  - `High` $\rightarrow$ 2

---

## 8. Model Training & Evaluation

We split the 1-million-row dataset into **75% Training** and **25% Testing** subsets using a `random_state` of 123 to ensure reproducibility. 

**Logistic Regression Results:**
- **Training Accuracy:** `59.97%`
- **Testing Accuracy:** `60.08%`

**Evaluation Check:** 
Because both accuracies are nearly identical (~60%), we successfully proved that our model is highly balanced. It is **not overfitting** (memorizing training data) and generalizes properly to unseen data.

---

## 9. Key Findings & Conclusions

1. **Volume Matters:** Over 1 million records processed successfully, revealing that the average GenZ user in our data is 20 years old and spends ~3.5 hours daily on platforms.
2. **Addiction Proportions:** A concerning 15.9% of the dataset exhibits a "High" addiction level, directly correlating with nighttime usage spikes.
3. **Model Integrity:** By relying on `daily_usage_hours`, `avg_session_minutes`, `gender`, and `addiction_level`, our Logistic Regression classifier established a reliable baseline (~60% accuracy) for predicting binary behaviors without overfitting.

---

<!-- _class: lead -->

# Thank You
### Questions & Discussion

*Open for questions regarding data preprocessing techniques, feature selection methodology, or potential future improvements (e.g., Random Forests, Hyperparameter Tuning).*