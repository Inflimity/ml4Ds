import pandas as pd
import numpy as np
import os

def generate_churn_data():
    """Generates a synthetic Customer Churn dataset for Level 5 Classification mission."""
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'CustomerID': range(1, n_samples + 1),
        'Age': np.random.randint(18, 70, n_samples),
        'Tenure': np.random.randint(0, 60, n_samples),
        'MonthlyCharges': np.random.uniform(20, 120, n_samples),
        'TotalCharges': np.random.uniform(100, 5000, n_samples),
        'IsContracted': np.random.choice([0, 1], n_samples),
        'SupportCalls': np.random.randint(0, 10, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Simple logic for Churn (target)
    # Higher support calls and no contract = High Churn probability
    df['Churn_Prob'] = (df['SupportCalls'] * 0.15) - (df['IsContracted'] * 0.4) + (df['MonthlyCharges'] * 0.002)
    df['Churn'] = (df['Churn_Prob'] > 0.4).astype(int)
    
    # Drop the helper column
    df = df.drop(columns=['Churn_Prob'])
    
    output_path = 'data/customer_churn.csv'
    df.to_csv(output_path, index=False)
    print(f"✅ Level 5 Data Generated: {output_path}")

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    generate_churn_data()
