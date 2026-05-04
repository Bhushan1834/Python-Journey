import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the inbuilt titanic dataset from seaborn
titanic = sns.load_dataset('titanic')

print("--- Titanic Dataset Preview ---")
print(titanic.head())

# Plotting the histogram for 'fare'
plt.figure(figsize=(10, 6))
sns.histplot(titanic['fare'], kde=True, bins=30, color='teal')

# Customizing the plot
plt.title('Distribution of Passenger Fares in Titanic', fontsize=15)
plt.xlabel('Fare', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Save the plot
plt.savefig('titanic_fare_distribution.png')
print("\nHistogram saved as 'titanic_fare_distribution.png'")

# Additional insight: Summary statistics for fare
print("\nSummary Statistics for Fare:")
print(titanic['fare'].describe())
