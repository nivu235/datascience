from sklearn.linear_model import LogisticRegression
import numpy as np
def get_input():
    usage = float(input("Enter usage minutes: "))
    duration = int(input("Enter contract duration"))
    return np.array([[usage,duration]])
def main():
    X = np.array([[100, 12], [200, 6], [50, 24], [300, 3]])  
    y = np.array([0, 1, 0, 1])  
    clf = LogisticRegression()
    clf.fit(X, y)
    features =get_input()
    predicted_churn = clf.predict(features)
    if predicted_churn== 0:
        print("The new customer is predicted not to churn.")
    else:
        print("The new customer is predicted to churn.")
main()


