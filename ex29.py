import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load a trained Logistic Regression model (replace with your actual model loading code)
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Get user input for feature and target variable names
feature_names = input("Enter the names of the features (comma-separated): ").split(',')
target_name = input("Enter the name of the target variable: ")

# Get the indices of selected features and target variable
selected_feature_indices = [iris.feature_names.tolist().index(feature) for feature in feature_names]
target_index = iris.target_names.tolist().index(target_name)

# Extract selected features and target variable
X_test_selected = X_test[:, selected_feature_indices]
y_test_selected = y_test == target_index  # Convert to binary classification

# Make predictions using the trained model
y_pred = model.predict(X_test_selected)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test_selected, y_pred)
precision = precision_score(y_test_selected, y_pred)
recall = recall_score(y_test_selected, y_pred)
f1 = f1_score(y_test_selected, y_pred)

# Display evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
