import csv
import random
from datetime import datetime, timedelta
import os

def generate_sales_data(num_records=1000):
    random.seed(42)
    
    start_date = datetime(2025, 1, 1)
    
    categories = ['Electronics', 'Clothing', 'Home', 'Toys']
    base_prices = {'Electronics': 200, 'Clothing': 50, 'Home': 100, 'Toys': 30}
    base_units = {'Electronics': 10, 'Clothing': 50, 'Home': 20, 'Toys': 40}
    
    data = []
    
    for i in range(num_records):
        # Dates
        current_date = start_date + timedelta(days=i)
        date_str = current_date.strftime('%Y-%m-%d')
        
        # Stores & Categories
        store_id = random.randint(1, 5)
        category = random.choice(categories)
        
        # Features
        is_holiday = current_date.weekday() >= 5 # Weekends as holidays/high traffic
        is_promotion = random.random() < 0.2
        
        # Base prices
        price = base_prices[category] * random.uniform(0.9, 1.1)
        
        # Hidden Pattern: Price Elasticity & Synergy with Promotions
        if is_promotion:
            price *= 0.8
            
        # Target: Units Sold
        units_sold = base_units[category]
        
        # Pattern 1: Seasonality
        if is_holiday:
            units_sold *= 1.5
            
        # Pattern 2: Price Elasticity
        if is_promotion:
            units_sold *= 2.5
            
        # Add random noise
        noise = random.gauss(0, units_sold * 0.1)
        units_sold = int(max(1, round(units_sold + noise)))
        
        revenue = round(units_sold * price, 2)
        price = round(price, 2)
        
        # Intentional Missing Data
        final_price = price if random.random() > 0.05 else ""  # 5% missing price
        final_store_id = store_id if random.random() > 0.03 else "" # 3% missing store
        
        data.append({
            'Date': date_str,
            'Store_ID': final_store_id,
            'Product_Category': category,
            'Price': final_price,
            'Is_Holiday': is_holiday,
            'Is_Promotion': is_promotion,
            'Units_Sold': units_sold,
            'Revenue': revenue
        })
        
    os.makedirs('data', exist_ok=True)
    
    with open('data/sales_dataset.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'Date', 'Store_ID', 'Product_Category', 'Price', 
            'Is_Holiday', 'Is_Promotion', 'Units_Sold', 'Revenue'
        ])
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Dataset generated successfully at 'data/sales_dataset.csv' with {num_records} records.")

if __name__ == '__main__':
    generate_sales_data()
