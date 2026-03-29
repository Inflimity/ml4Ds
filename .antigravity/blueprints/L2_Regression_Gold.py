import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def level_2_solution():
    """
    GOLD STANDARD: Level 2 - The Junior Scientist
    Objective: Implement the Split and the First Regression.
    """
    # 1. Load the results from Level 1
    df = pd.read_csv('cleaned_data.csv')
    
    # 2. Extract the features (X) and the target (y)
    # We use numerical columns to avoid complexities here
    X = df.drop(columns=['units_sold', 'product_category'])
    y = df['units_sold']
    
    # 3. Perform the Split (Crucial step)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train the Model (Linear Regression)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 5. Evaluate the model
    # Benchmarks: R2 score should be > 0.7 for the Sales dataset.
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"DEBUG: R-Squared: {r2:.2f}")
    print(f"DEBUG: MSE: {mse:.2f}")
    
    return r2, mse

if __name__ == "__main__":
    level_2_solution()
