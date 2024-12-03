import pandas as pd

# Load the dataset
file_path = '/Users/macbookpro/Documents/ML Project 1/garments_worker_productivity.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Handle missing values in the 'wip' column by imputing with the median
if 'wip' in data.columns:
    median_wip = data['wip'].median()
    data['wip'] = data['wip'].fillna(median_wip)
    print(f"Missing values in 'wip' column have been replaced with median: {median_wip}")
else:
    print("'wip' column not found in the dataset.")

# Detect and handle outliers using the interquartile range (IQR) method
def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Capping outliers
    df[column] = df[column].apply(
        lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x)
    )
    print(f"Outliers in '{column}' have been capped.")

# Handle outliers in specific columns
columns_to_check = ['idle_time', 'incentive', 'actual_productivity']
for column in columns_to_check:
    if column in data.columns:
        handle_outliers(data, column)
    else:
        print(f"Column '{column}' not found in the dataset.")

# Save the updated dataset to a new file
output_path = '/Users/macbookpro/Documents/ML Project 1/cleaned_garments_worker_productivity.xlsx'
data.to_excel(output_path, index=False)
print(f"Updated dataset saved to {output_path}")
