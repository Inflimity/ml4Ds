import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def level_5_solution():
    """
    GOLD STANDARD: Level 5 - The Master Architect
    Objective: Implement Binary Classification on Churn.
    """
    # 1. Load the generated churn data
    df = pd.read_csv('data/customer_churn.csv')
    
    # 2. Select the features (X) and the target (y)
    X = df.drop(columns=['CustomerID', 'Churn'])
    y = df['Churn']
    
    # 3. Perform the Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train the Model (Logistic Regression)
    # Benchmarks: Imbalanced data check.
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # 5. Evaluate the model
    # Benchmarks: Accuracy is misleading if data is imbalanced.
    # Check the Confusion Matrix for False Negatives.
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions)
    
    print(f"DEBUG: Logistic Accuracy: {accuracy:.2f}")
    print(f"DEBUG: Confusion Matrix:\n{matrix}")
    
    return accuracy, matrix

if __name__ == "__main__":
    level_5_solution()
