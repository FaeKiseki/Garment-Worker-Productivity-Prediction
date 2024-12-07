import pandas as pd

# Load the dataset
file_path = '/Users/macbookpro/Documents/ML Project 1/cleaned_garments_worker_productivity.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Perform one-hot encoding for categorical features
categorical_features = ['quarter', 'department', 'day']
data = pd.get_dummies(data, columns=categorical_features, drop_first=True)
print("One-hot encoding applied to categorical features:", categorical_features)

# Convert 'date' column to datetime format and extract additional features
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Convert to datetime format
    data['month'] = data['date'].dt.month  # Extract the month
    data['day_of_week'] = data['date'].dt.dayofweek  # Extract the day of the week (0=Monday, 6=Sunday)
    print("Date features extracted: month, day_of_week")
else:
    print("'date' column not found in the dataset.")

# Drop the original 'date' column if not required anymore
data.drop(columns=['date'], inplace=True)
print("'date' column dropped after feature extraction.")

# Save the updated dataset to a new file
output_path = '/Users/macbookpro/Documents/ML Project 1/engineered_garments_worker_productivity.xlsx'
data.to_excel(output_path, index=False)
print(f"Feature-engineered dataset saved to {output_path}")
