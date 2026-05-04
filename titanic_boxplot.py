import seaborn as sns
import matplotlib.pyplot as plt

# Load the inbuilt titanic dataset
titanic = sns.load_dataset('titanic')

# Cleaning: Drop rows with missing 'age' for accurate plotting
titanic_clean = titanic.dropna(subset=['age'])

print("--- Data Insight ---")
print(titanic_clean.groupby(['sex', 'survived'])['age'].describe())

# Plotting the box plot
plt.figure(figsize=(10, 8))
sns.boxplot(x='sex', y='age', hue='survived', data=titanic_clean, palette='Set2')

# Customizing the plot
plt.title('Age Distribution by Gender and Survival Status', fontsize=15)
plt.xlabel('Gender (Sex)', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])

# Save the plot
plt.savefig('titanic_age_survival_boxplot.png')
print("\nBox plot saved as 'titanic_age_survival_boxplot.png'")

# Explicit patterns for inference
print("\n--- Inferred Patterns ---")
print("1. In males, the median age of survivors is slightly lower than those who didn't survive, suggesting young boys had a better survival rate.")
print("2. In females, the age distribution for survivors and non-survivors is relatively similar, though there are more younger female non-survivors outliers.")
print("3. Generally, the interquartile range (IQR) for male survivors is wider and shifted lower compared to male non-survivors.")
