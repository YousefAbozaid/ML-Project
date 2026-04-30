# Presentation Script: Predicting Medical Costs

*Note: You can adjust the speakers depending on your team size.*

---

## Slide 1: Title Slide
**[Speaker 1]**
"Hi everyone, thanks for coming. We're [Team Name], and today we're walking you through our project: 'Predicting Medical Costs'. Our team is [list members]. Let’s get started."

---

## Slide 2: Challenge Description & Goal
**[Speaker 1]**
"For this project, we wanted to look at medical data to see what actually drives up healthcare costs, and then build a model to predict those charges. 

This is important because if insurance providers know exactly what causes higher costs, they can price premiums more fairly and figure out the best ways to encourage healthier habits."

---

## Slide 3: Dataset Overview
**[Speaker 2]**
"Thanks [Speaker 1]. We used the 'Medical Cost Personal Datasets' from Kaggle for this. 

It's a pretty straightforward dataset. It gives us info on patients like Age, Sex, BMI, number of kids, region, and whether they smoke. The main thing we wanted to predict—our target variable—is the 'Charges' column, which is the actual amount billed to insurance."

---

## Slide 4: Data Cleaning & Preprocessing
**[Speaker 2]**
"Before we got to the fun part, we had to clean the data. 

Luckily, we didn't have any missing values. We just had to drop a few duplicate rows to keep things accurate. Then, since our model can't read text, we had to encode our categorical variables. Basically, we turned columns like 'sex', 'smoker', and 'region' into numbers so the algorithm could process them."

---

## Slide 5: Exploratory Data Analysis - Key Trends
**[Speaker 3]**
"Once the data was ready, we started looking for trends. 

In this first chart showing medical charges, you can see it's skewed to the right. Most people have lower costs, but there’s a small group with extremely high bills. 

The second chart highlights something big: the difference between smokers and non-smokers. Looking at the boxplot, smokers' median charges are way higher. It was pretty obvious early on that smoking is a massive factor here."

---

## Slide 6: Exploratory Data Analysis - Deep Dive
**[Speaker 4]**
"We wanted to look a bit closer, so we plotted medical charges against age, and separated the points by smoking status. 

There are two main takeaways here. First, costs go up steadily as people age, which isn't surprising. Second, and more importantly, smoking creates a huge gap. At literally every age, smokers form their own distinct group with much higher costs than non-smokers."

---

## Slide 7: Modeling Approach
**[Speaker 5]**
"With a good grasp on the data, we moved on to the machine learning side. 

We decided to use a Random Forest Regressor. We used 80% of our data to train it, and kept the remaining 20% to test it. We went with Random Forest because it's really good at picking up on complex patterns—like how age, BMI, and smoking interact—and it also lets us see which features are the most important."

---

## Slide 8: Prediction Results & Evaluation
**[Speaker 5]**
"The model actually performed really well. 

We got an R-squared score of about 0.83. Basically, our model can explain roughly 83% of the differences in medical charges just based on the few columns we gave it. 

When we checked the 'Feature Importance', 'Smoker Status' was definitely the biggest factor the model used, followed by 'BMI' and 'Age'."

---

## Slide 9: Actionable Insights & Recommendations
**[Speaker 6]**
"To wrap things up, we have a few practical takeaways based on our model:

1. **Focus on Smoking:** Since smoking is the biggest driver of costs, offering incentives to quit or free wellness programs could save a lot of money.
2. **Targeted Health Campaigns:** BMI was the next biggest factor. Programs focused on weight management could help prevent chronic issues down the road.
3. **Pricing Premiums:** Insurance companies can use models like this to adjust pricing, so the financial risk tied to smoking and high BMI is priced more accurately.

Basically, preventative care isn't just good for the patients; it makes the most sense financially too."

---

## Slide 10: Q&A
**[Speaker 1 or All]**
"That’s it for our presentation. Thanks for listening. We'd be happy to answer any questions you have about what we did or what we found."