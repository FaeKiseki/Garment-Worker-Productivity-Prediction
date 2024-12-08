import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/macbookpro/Documents/ML Project 1/scaled_garments_worker_productivity.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Plot the distribution of the target variable
plt.figure(figsize=(10, 6))
sns.histplot(data['actual_productivity'], kde=True, bins=30, color='blue')
plt.title('Distribution of Actual Productivity', fontsize=16)
plt.xlabel('Actual Productivity', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Calculate and display key statistics
mean_value = data['actual_productivity'].mean()
median_value = data['actual_productivity'].median()
std_dev = data['actual_productivity'].std()

print(f"Mean of Actual Productivity: {mean_value:.2f}")
print(f"Median of Actual Productivity: {median_value:.2f}")
print(f"Standard Deviation of Actual Productivity: {std_dev:.2f}")
