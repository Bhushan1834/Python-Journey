import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
try:
    df = sns.load_dataset('iris')
    print("Iris dataset loaded from Seaborn.\n")
except:
    url = "https://raw.githubusercontent.com/uiuc-cse/dataset-iris/master/iris.csv"
    df = pd.read_csv(url)
    print("Iris dataset loaded from URL.\n")

print("--- Step 1: Feature Types ---")
print(df.info())
print("\nFeature Types:")
print(df.dtypes)

print("\n--- Step 2: Distribution Analysis (Histograms) ---")
# Plotting histograms for all numeric features
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

plt.figure(figsize=(12, 10))
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(2, 2, i)
    sns.histplot(df[column], kde=True, color='skyblue')
    plt.title(f'Histogram of {column}')

plt.tight_layout()
plt.savefig('iris_histograms.png')
print("Histograms saved as 'iris_histograms.png'")

print("\n--- Step 3: Outlier Identification (Boxplots) ---")
plt.figure(figsize=(12, 10))
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(y=df[column], color='lightgreen')
    plt.title(f'Boxplot of {column}')

plt.tight_layout()
plt.savefig('iris_boxplots.png')
print("Boxplots saved as 'iris_boxplots.png'")

print("\n--- Step 4: Outlier Comparison & Analysis ---")
# Function to calculate outliers using IQR
def get_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower) | (data[column] > upper)]
    return outliers

for column in numeric_columns:
    outliers = get_outliers(df, column)
    if not outliers.empty:
        print(f"Detected {len(outliers)} outliers in '{column}':")
        print(outliers[column].values)
    else:
        print(f"No outliers detected in '{column}'.")

print("\nInference:")
print("- Sepal Width is the only feature with significant outliers (representing extreme variances in flower width).")
print("- Petal Length and Petal Width show bimodal distributions, indicating clear separation between species (e.g., Setosa vs others).")
print("- Sepal Length follows a distribution relatively close to normal.")
