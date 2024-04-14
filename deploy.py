
import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_curve, roc_auc_score, confusion_matrix
import joblib
from imblearn.over_sampling import SMOTE


# Load the saved model
with open('random_forest.pkl', 'rb') as f:
    model = joblib.load(f)

# Define the Streamlit app
def main():
    st.title('Customer Churn Prediction')

    # Upload the test data
    uploaded_file = st.file_uploader("Upload your CSV file for prediction:", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

        # Make predictions
        X_test = df.drop('churn', axis=1)
        y_test = df['churn']
        y_pred = model.predict(X_test)

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)
        cf_matrix = confusion_matrix(y_test, y_pred)

        # Display evaluation metrics
        st.write(f"Accuracy: {accuracy}")
        st.write(f"Recall: {recall}")
        st.write(f"Precision: {precision}")
        st.write(f"F1 Score: {f1}")
        st.write(f"ROC AUC Score: {roc_auc}")

        # Plot confusion matrix
        st.write("Confusion Matrix:")
        st.write(cf_matrix)

if __name__ == "__main__":
    main()