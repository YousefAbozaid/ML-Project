# Football Players Data Analysis Presentation

## 1. Introduction
- **Goal**: Analyze the FIFA Football Players dataset to uncover insights, visualize trends, and build a predictive model.
- **Dataset**: Comprehensive stats of football players (Age, Height, Weight, Value, Wage, Foot preference, Ratings).
- **Target**: Predict whether a player is "High Rated" (Overall Rating $\ge$ 80).

## 2. Data Cleaning
- Addressed missing values by filling numerical features with the median and categorical features with the mode.
- Dropped irrelevant columns (e.g., Name, Birth Date, National Team details, Body Type) to focus on raw player attributes.
- Ensured no duplicate data entries were present.

## 3. Exploratory Data Analysis (EDA)
- **Age Distribution**: Most players fall within the 20-30 age range.
- **Preferred Foot**: A significant majority of players (approx. 76%) prefer their Right foot.
- **Ratings**: Ratings follow a normal distribution centered around 66.
- **Correlation**: High positive correlation between a player's potential, wage, value, and their overall rating.

## 4. Feature Selection
- Selected key features for modeling: `age`, `height_cm`, `weight_kgs`, `potential`, `value_euro`, `wage_euro`, `preferred_foot`, and `international_reputation(1-5)`.
- Created target variable `High_Rating` based on `overall_rating >= 80`.
- Applied Label Encoding to map categorical variable `preferred_foot` (Right: 0, Left: 1).

## 5. Modeling and Prediction
- Split the dataset into 80% Training and 20% Testing sets.
- Employed **Logistic Regression** as the binary classifier.
- **Results**: High accuracy in predicting Top Rated players based heavily on their monetary values (wage and value) and potential.
- **Evaluation**: The model provides actionable insights for scouting by demonstrating that a combination of potential, market value, and physical stats reliably predict top-tier player status.

## 6. Actionable Insights
- **Scouting focus**: High potential correlates strongly with future high ratings. Identifying young players with high potential but current low wage is optimal for investments.
- **Market Value alignment**: Wage and Value are strongly tied to the overall rating. Outliers (low rating, high wage) should be investigated for club cost-savings.