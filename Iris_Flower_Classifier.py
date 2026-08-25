 # train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import streamlit as st
import numpy as np
# 1. Load dataset
iris = load_iris()
X, y = iris.data, iris.target 

# 2. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "iris_model.pkl")

model = joblib.load("iris_model.pkl")

print("Model trained and saved as iris_model.pkl")
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="flower",
    layout="centered"
)

st.title("Iris Flower Classifier")
st.caption("Classify Iris Flowers By length and width")

st.divider()
st.write("Enter flower measurement to predict the species.")

Sepal_length=st.number_input("Enter Sepal length in(cm):",min_value=0.2,max_value=10.00)
Sepal_width=st.number_input("Enter Sepal width in(cm):",min_value=0.2,max_value=10.00)
Petal_length=st.number_input("Enter Petal length in(cm):",min_value=0.2,max_value=10.00)
Petal_width=st.number_input("Enter Petal width in(cm):",min_value=0.2,max_value=10.00)



if st.button("Predict Species"):
    features = np.array([[Sepal_length, Sepal_width, Petal_length, Petal_width]])
    prediction = model.predict(features)[0]
    species = ["Setosa", "Versicolor", "Virginica"][prediction]

    st.success(f"Predicted Species: **{species}**")
