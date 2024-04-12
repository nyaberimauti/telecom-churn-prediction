

# Telecom Churn Prediction
## Project Overview
Churn refers to customers who discontinue using a particular service. The objective of this project is to predict churn and identify the features that contribute to customer attrition. Accurately predicting churn can provide valuable insights to business owners, enabling them to develop effective marketing strategies and enhance customer retention efforts for improved profitability.
 
## Components
**Jupyter Notebook**

**Presentation**

**Data**

## Technologies/Packages
The project leverages several technologies and Python packages, including:

- Python  version: 3.6.9
- Matplotlib version: 3.1.3
- Seaborn version: 0.9.0
- Pandas  version: 0.25.1
- Numpy version: 1.16.5
- Scikit-learn version: 0.21.
## 1 Data Preprocessing
- In this phase, we will focus on several tasks to prepare our data for analysis and modeling. This includes data cleaning, handling missing values, transforming data, addressing duplicates, reshaping the data, and other necessary processes to ensure that our dataset is clean, structured, and suitable for further analysis and modeling..
# Exploratory Data Analysis (EDA)
During the EDA phase, we will delve into the dataset to gain insights and understanding of its various features. We will employ data visualization techniques to uncover trends, patterns, and relationships within the data. Additionally, we will perform feature engineering to create new features from existing ones and utilize one-hot encoding to handle categorical variables as needed for our analysis and modeling tasks.


## Features with a Significant Impact on Churn
**Daily Charge**: The amount customers are charged daily was found to have a significant influence on churn. Higher daily charges were associated with a higher likelihood of customers churning.

**Customer Service Calls**: The number of customer service calls made by customers also played a notable role in churn prediction. Customers who made more frequent calls to customer service were more likely to churn.

**Data Usage**: Data usage patterns emerged as another important factor affecting churn. Customers with specific data usage behaviors were more prone to churn compared to others.

## Modeling Overview
I explored various machine learning models to predict customer churn, each offering different accuracies and insights:

**Logistic Regression**: Achieved an accuracy of around 70%.

**Decision Tree Classifier**: Achieved an accuracy of approximately 88%.

**Random Forest Classifier**: Achieved an accuracy of about 92%.

**Voting Classifier**: Combined multiple models to achieve an accuracy of around 91%.

**Final Model with SMOTE**: Utilized SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalance and achieved an accuracy of 90%.

## Conclusions
Customer churn is significantly influenced by `daily charges`, `customer service calls`, and `data usage patterns`.

Recommendations for business owners based on the analysis:

`Improve Customer Service`: Address the issues identified with customer service calls to enhance customer satisfaction and retention.

`Revise Daily Charges`: Evaluate and potentially adjust the daily charges to align better with customer expectations and market standards.
## Next Steps
Model Deployment