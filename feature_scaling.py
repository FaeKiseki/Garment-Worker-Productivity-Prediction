import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = '/Users/macbookpro/Documents/ML Project 1/engineered_garments_worker_productivity.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Identify numerical columns
numerical_features = [
    'team', 'targeted_productivity', 'smv', 'wip', 'over_time', 'incentive',
    'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers', 'actual_productivity'
]

# Initialize StandardScaler
scaler = StandardScaler()

# Scale numerical features
data[numerical_features] = scaler.fit_transform(data[numerical_features])
print(f"Numerical features scaled: {numerical_features}")

# Save the scaled dataset to a new file
output_path = '/Users/macbookpro/Documents/ML Project 1/scaled_garments_worker_productivity.xlsx'
data.to_excel(output_path, index=False)
print(f"Scaled dataset saved to {output_path}")
