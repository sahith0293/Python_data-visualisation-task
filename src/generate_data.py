import pandas as pd
import numpy as np

# Create sample data
np.random.seed(0)
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books']
months = pd.date_range(start='2023-01-01', periods=12, freq='ME').strftime('%B').tolist()

data = {
    'Category': np.random.choice(categories, 1000),
    'Month': np.random.choice(months, 1000),
    'Sales': np.random.randint(100, 1000, 1000),
    'Profit': np.random.randint(10, 500, 1000)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('../data/sample_data.xlsx', index=False)