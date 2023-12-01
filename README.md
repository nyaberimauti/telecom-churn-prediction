 # telecom-churn-prediction

# Telecom Churn Prediction

## Project Overview
#### A Churn is someone who stops to use a given service. The goal of this project is to predict churn, and what may be features that can lead to customer churning. Accurately predicting, will help business owners to find insights and come up with a marketing strategy. This will help them to understand ways they can retain customers for profitability
 ## Components
 `Jupyter Notebook` The Jupyter Notebook is our key deliverable and contains details of our approach and methodology, data cleaning, exploratory data analysis, and model building and validation.

`Presentation` The presentation gives a high-level overview of our approach, findings, and recommendations for non-technical stakeholders. It is aimed to be between 5 and 10 minutes long.

`Data`

The dataset can be found in the file `telecom-churn.csv` in the Data folder, in this repository. It was originally provided in the following repository.
## Technologies/ Packages

- Python  version: 3.6.9
- Matplotlib version: 3.1.3
- Seaborn version: 0.9.0
- Pandas  version: 0.25.1
- Numpy version: 1.16.5
- Scikit-learn version: 0.21.
## 1 Data Preprocessing
- Here we will work on data cleaning, handling missing values, data transformation, handling duplicates, data reshaping, and other processes to ensure that we have a clean, structured, and suitable format for analysis and modeling.
# Exploratory Data Analysis (EDA)
Here we will explore the different features of the dataset to gain a better understanding of the data. We will use data visualization to uncover trends and patterns. We will use Feature Engineering to create new features from existing ones and perform One-Hot Encoding on categorical variables that we will require for analysis.

### Features with a big impact on churn include
`Daily charge`
`Customer service calls`
`Data usage`
- We found out that daily charges had a big influence on customer churn

## Modeling
### The following are the different types of models I used:
- `Logistic Regression` with an accuracy of approximately 70%
- ` Decision Tree Classifier` with an accuracy of approximately 88%
- `Random Forest Classifier` with an accuracy of approximately 92%
- ` Voting Classifier` with an accuracy of approximately 91%
- `Final model by using SMOTE` with an accuracy of 90%
# Conclusions
#### Churn is highly affected by daily charges, customer service calls, and data usage by customers.
#### The business owners should improve their customer services
#### Should revise daily charges on customers
