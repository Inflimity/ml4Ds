import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def level_4_solution():
    """
    GOLD STANDARD: Level 4 - The ML Engineer
    Objective: Implement an Ensemble Model (Random Forest) for Taxi Fares.
    """
    # 1. Load the cleaned taxi data from Level 3
    df = pd.read_csv('cleaned_taxis.csv')
    
    # 2. Select the features (X) and the target (y)
    # Target is the total fare
    # Drop timestamp and non-numeric columns
    X = df.select_dtypes(include=['float64', 'int64', 'bool', 'uint8'])
    X = X.drop(columns=['total', 'fare', 'tip', 'tolls', 'passengers'])
    y = df['total']
    
    # 3. Perform the Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train the Model (Random Forest Regressor)
    # Benchmarks: RF should outperform Linear Regression here.
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Evaluate the model
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"DEBUG: Random Forest R-Squared: {r2:.2f}")
    return r2, mse

if __name__ == "__main__":
    level_4_solution()
