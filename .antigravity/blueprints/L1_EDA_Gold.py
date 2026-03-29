import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def level_1_solution():
    """
    GOLD STANDARD: Level 1 - The Analyst
    Objective: Clean the sales data and find the strongest signal.
    """
    # 1. Load the raw data
    df = pd.read_csv('data/sales_dataset.csv')
    
    # 2. Identify the target
    target = 'units_sold'
    
    # 3. Clean the data (Gold standard: handling categories)
    # We keep only numeric columns for correlation analysis
    numeric_cols = df.select_dtypes(include=['float64', 'int64', 'bool'])
    
    # 4. Correlation Analysis
    corr_matrix = numeric_cols.corr()
    
    # Benchmarks:
    # 'price' should have a strong negative correlation with units_sold.
    # 'is_promotion' should have a strong positive correlation.
    
    advertising_corr = corr_matrix['units_sold'].get('is_promotion', 0)
    price_corr = corr_matrix['units_sold'].get('price', 0)
    
    print(f"DEBUG: Promotion Correlation: {advertising_corr:.2f}")
    print(f"DEBUG: Price Correlation: {price_corr:.2f}")
    
    # 5. Save the cleaned data for Level 2
    # In a real scenario, we might also drop 'revenue' as it's a data leak (Units * Price)
    df_cleaned = df.drop(columns=['revenue', 'date', 'store_id'])
    df_cleaned.to_csv('cleaned_data.csv', index=False)
    
    return corr_matrix

if __name__ == "__main__":
    level_1_solution()
