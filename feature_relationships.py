import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/macbookpro/Documents/ML Project 1/scaled_garments_worker_productivity.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Scatter plots to visualize relationships
features_to_plot = ['over_time', 'incentive', 'smv']

for feature in features_to_plot:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=feature, y='actual_productivity', alpha=0.6, color='blue')
    plt.title(f'Relationship between Actual Productivity and {feature}', fontsize=16)
    plt.xlabel(feature, fontsize=14)
    plt.ylabel('Actual Productivity', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Box plots to analyze distributions
for feature in features_to_plot:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=feature, y='actual_productivity', palette='Blues')
    plt.title(f'Distribution of Actual Productivity by {feature}', fontsize=16)
    plt.xlabel(feature, fontsize=14)
    plt.ylabel('Actual Productivity', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
