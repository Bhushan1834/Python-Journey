import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a synthetic Academic Performance dataset
np.random.seed(42)
n_students = 50

data = {
    'Student_ID': range(1, n_students + 1),
    'Gender': np.random.choice(['M', 'F', 'male', 'female', 'F '], n_students), # Inconsistent strings
    'Math_Score': np.random.randint(40, 100, n_students).astype(float),
    'Science_Score': np.random.randint(40, 100, n_students).astype(float),
    'Reading_Score': np.random.randint(40, 100, n_students).astype(float),
    'Attendance': np.random.randint(60, 100, n_students),
    'Study_Hours': np.random.lognormal(mean=1, sigma=0.8, size=n_students) # Skewed data
}

df = pd.DataFrame(data)

# Introduce Missing Values
df.loc[5, 'Math_Score'] = np.nan
df.loc[15, 'Science_Score'] = np.nan
df.loc[25, 'Reading_Score'] = np.nan

# Introduce Outliers
df.loc[10, 'Math_Score'] = 180 # High outlier
df.loc[20, 'Math_Score'] = -50  # Low outlier
df.loc[30, 'Science_Score'] = 200 # High outlier

print("--- Original Dataset Sample ---")
print(df.head())
print("\n")

print("--- Step 1: Handling Missing Values and Inconsistencies ---")
# 1.1 Checking for missing values
print("Missing Values before cleaning:")
print(df.isnull().sum())

# Handling missing values using median (robust to outliers)
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].median())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].median())
df['Reading_Score'] = df['Reading_Score'].fillna(df['Reading_Score'].median())

# 1.2 Handling inconsistencies in 'Gender'
print("\nUnique values in Gender before cleaning:", df['Gender'].unique())
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender'] = df['Gender'].replace({'m': 'Male', 'male': 'Male', 'f': 'Female', 'female': 'Female'})
print("Unique values in Gender after cleaning:", df['Gender'].unique())

print("\n--- Step 2: Handling Outliers ---")
# 2.1 Identify outliers in Math_Score using IQR (Interquartile Range)
Q1 = df['Math_Score'].quantile(0.25)
Q3 = df['Math_Score'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Math_Score IQR: {IQR}, Bounds: [{lower_bound}, {upper_bound}]")
outliers = df[(df['Math_Score'] < lower_bound) | (df['Math_Score'] > upper_bound)]
print(f"Number of outliers detected in Math_Score: {len(outliers)}")

# Strategy: Capping outliers to the upper and lower bounds (Winsorization)
df['Math_Score'] = np.clip(df['Math_Score'], lower_bound, upper_bound)
print("Outliers in Math_Score have been capped to bounds.")

# Repeat for Science_Score
Q1_s = df['Science_Score'].quantile(0.25)
Q3_s = df['Science_Score'].quantile(0.75)
IQR_s = Q3_s - Q1_s
df['Science_Score'] = np.clip(df['Science_Score'], Q1_s - 1.5 * IQR_s, Q3_s + 1.5 * IQR_s)

print("\n--- Step 3: Data Transformations ---")
# 3.1 Decrease Skewness using Log Transformation on 'Study_Hours'
print(f"Skewness of Study_Hours before transformation: {df['Study_Hours'].skew():.2f}")

# Adding a small constant to avoid log(0) if any values were 0
df['Log_Study_Hours'] = np.log1p(df['Study_Hours'])

print(f"Skewness of Log_Study_Hours after transformation: {df['Log_Study_Hours'].skew():.2f}")

# 3.2 Feature Scaling (Normalization) on Attendance
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['Attendance_Normalized'] = scaler.fit_transform(df[['Attendance']])

print("\n--- Final Cleaned and Transformed Dataset Sample ---")
print(df[['Student_ID', 'Gender', 'Math_Score', 'Log_Study_Hours', 'Attendance_Normalized']].head())

# Save to CSV
df.to_csv("academic_performance_cleaned.csv", index=False)
print("\nCleaned dataset saved to academic_performance_cleaned.csv")
