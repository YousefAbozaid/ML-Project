import json

notebook = {
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.8"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# 1- Load and understanding data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "df = pd.read_csv('dataset/fifa_players.csv')\n",
        "df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "df.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# 2- Cleaning data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "df.duplicated().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "df.isnull().sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### Drop unuseful columns"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "columns_to_drop = ['name', 'full_name', 'birth_date', 'nationality', 'positions', \n",
        "                   'body_type', 'national_team', 'national_team_position']\n",
        "df.drop(columns=columns_to_drop, inplace=True, errors='ignore')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### Handle Missing Values using Median and Mode"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "for col in df.select_dtypes(include='number').columns:\n",
        "    df[col] = df[col].fillna(df[col].median())\n",
        "\n",
        "for col in df.select_dtypes(include='object').columns:\n",
        "    df[col] = df[col].fillna(df[col].mode()[0])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "df.isnull().sum().sum() # Check if any nulls remain"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# 3- Visualization to explore and Feature Selection"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "sns.countplot(x=df['preferred_foot'])\n",
        "plt.title('Count of Players by Preferred Foot')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "sns.boxplot(x=df['age'])\n",
        "plt.title('Boxplot of Age')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "plt.hist(df['overall_rating'], bins=20)\n",
        "plt.title('Distribution of Overall Rating')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "count_foot = df['preferred_foot'].value_counts()\n",
        "plt.pie(count_foot, autopct='%.2f%%', labels=['Right', 'Left'])\n",
        "plt.title('Preferred Foot Distribution')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### Feature Selection & Correlation"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "number_columns = df.select_dtypes(include='number')\n",
        "corr_matrix = number_columns.corr()\n",
        "corr_matrix['overall_rating'].sort_values(ascending=False).head(10)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### Creating a Target Variable: High_Rating (1 if overall_rating >= 80 else 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "new_df = df[['age', 'height_cm', 'weight_kgs', 'potential', 'value_euro', 'wage_euro', 'preferred_foot', 'international_reputation(1-5)', 'overall_rating']].copy()\n",
        "new_df['High_Rating'] = (new_df['overall_rating'] >= 80).astype(int)\n",
        "new_df.drop('overall_rating', axis=1, inplace=True)\n",
        "new_df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# 4- Modeling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### Encoding Categorical Data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "new_df['preferred_foot'] = new_df['preferred_foot'].map({'Right': 0, 'Left': 1})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score, classification_report"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Split data\n",
        "X = new_df.drop(['High_Rating'], axis=1)\n",
        "y = new_df['High_Rating']\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Build model and fit\n",
        "model = LogisticRegression(max_iter=1000)\n",
        "model.fit(X_train, y_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Prediction\n",
        "y_pred = model.predict(X_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Evaluation\n",
        "acc = accuracy_score(y_test, y_pred)\n",
        "print(f'Accuracy: {acc:.4f}')\n",
        "print(classification_report(y_test, y_pred))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# 5- Present findings in a well-structured report\n",
        "Please refer to the accompanying presentation slides for the detailed findings."
      ]
    }
  ]
}

with open('/home/yousef/ML-project/ml/football_players_project.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

