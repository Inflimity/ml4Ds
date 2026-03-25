import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('data/sales_dataset.csv')

# Let's drop missing data just for the correlation math
numeric_df = df.select_dtypes(include=['float64', 'int64', 'bool'])
correlation_matrix = numeric_df.corr()

# 3. Plot the heatmap!
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap: What drives Units Sold?")

# Saving as an image so you can view it directly in your workspace
plt.savefig('heatmap.png', bbox_inches='tight')
print("Successfully generated and saved heatmap.png!")
