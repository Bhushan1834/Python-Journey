import pandas as pd
import seaborn as sns

# Load the Iris dataset from Seaborn or a public URL
# Seaborn is usually the easiest way to get the Iris dataset
try:
    df = sns.load_dataset('iris')
    print("Iris dataset loaded from Seaborn.\n")
except:
    url = "https://raw.githubusercontent.com/uiuc-cse/dataset-iris/master/iris.csv"
    df = pd.read_csv(url)
    print("Iris dataset loaded from URL.\n")

print("--- Step 1: Summary Statistics Grouped by Species ---")
# Providing mean, median, min, max, and std for numeric variables grouped by 'species'
grouped_stats = df.groupby('species').agg(['mean', 'median', 'min', 'max', 'std'])

print("Grouped Summary Statistics (first few columns):")
print(grouped_stats.head())
print("\n")

# Alternatively, a more readable view using describe()
print("Detailed Summary using describe() grouped by Species:")
print(df.groupby('species').describe())
print("\n")

print("--- Step 2: Basic Statistical Details for Specific Species ---")
# Specifying the species list manually as requested
# Note: Seaborn's dataset labels are 'setosa', 'versicolor', 'virginica'
# Some CSVs use 'Iris-setosa' etc. We'll handle both.

species_to_analyze = df['species'].unique()

for species in species_to_analyze:
    print(f"--- Statistics for Species: {species} ---")
    species_df = df[df['species'] == species]
    
    # Displaying mean, std, and percentiles (25%, 50%, 75%)
    # describe() includes these by default
    stats = species_df.describe()
    
    # Selecting the specific metrics requested
    selected_stats = stats.loc[['mean', 'std', '25%', '50%', '75%']]
    print(selected_stats)
    print("\n")

# Example of manual calculation for mean and std as requested in the program logic
print("--- Manual Calculation for specific species ('Setosa') ---")
setosa_data = df[df['species'] == species_to_analyze[0]]
print(f"Mean (Petal Length): {setosa_data['petal_length'].mean():.2f}")
print(f"Std Deviation (Petal Length): {setosa_data['petal_length'].std():.2f}")
print(f"75th Percentile (Petal Length): {setosa_data['petal_length'].quantile(0.75):.2f}")
