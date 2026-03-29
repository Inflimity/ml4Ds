import pandas as pd
import numpy as np

def level_3_solution():
    """
    GOLD STANDARD: Level 3 - The Statistician
    Objective: Extract features from timestamps (Taxis dataset).
    """
    # 1. Load the raw taxi data
    df = pd.read_excel('data/Taxis_Data.xlsx')
    
    # 2. Extract features from 'pickup' timestamp (Crucial step)
    df['pickup'] = pd.to_datetime(df['pickup'])
    df['pickup_hour'] = df['pickup'].dt.hour
    df['pickup_day'] = df['pickup'].dt.dayofweek
    df['is_weekend'] = (df['pickup_day'] >= 5).astype(int)
    
    # 3. Clean the labels (Check for NaNs)
    df = df.dropna(subset=['total'])
    
    # 4. Handle Categorical columns (Boroughs)
    # Simple label encoding or dummy variables
    df = pd.get_dummies(df, columns=['pickup_borough', 'dropoff_borough'], drop_first=True)
    
    # 5. Benchmarks:
    # Does pickup_hour have a strong relationship with total fare?
    print(f"DEBUG: Feature Extraction Completed for Taxis.")
    print(f"DEBUG: New Features: {df[['pickup_hour', 'is_weekend']].head()}")
    
    # Save the cleaned taxi data for Level 4
    df.to_csv('cleaned_taxis.csv', index=False)
    
    return True

if __name__ == "__main__":
    level_3_solution()
