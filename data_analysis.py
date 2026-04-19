import pandas as pd
import numpy as np

# 1. Import all required Python Libraries
# Already imported above: pandas and numpy

print("--- Step 2: Loading Dataset ---")
# 2. Locate and load an open-source dataset into a pandas dataframe
# Using the Titanic dataset from a public URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print("Dataset loaded successfully.\n")

print("--- Step 3: Data Preprocessing ---")
# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())
print("\n")

# Use describe() for statistics
print("Descriptive Statistics:")
print(df.describe(include='all'))
print("\n")

# Provide variable descriptions
variable_descriptions = {
    "PassengerId": "Unique identifier for each passenger",
    "Survived": "Survival status (0 = No, 1 = Yes)",
    "Pclass": "Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)",
    "Name": "Passenger Name",
    "Sex": "Passenger Gender",
    "Age": "Passenger Age",
    "SibSp": "Number of Siblings/Spouses aboard",
    "Parch": "Number of Parents/Children aboard",
    "Ticket": "Ticket Number",
    "Fare": "Passenger Fare",
    "Cabin": "Cabin Number",
    "Embarked": "Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)"
}
print("Variable Descriptions:")
for var, desc in variable_descriptions.items():
    print(f"- {var}: {desc}")
print("\n")

print("--- Step 4: Data Formatting and Normalization ---")
# Check data types
print("Initial Data Types:")
print(df.dtypes)
print("\n")

# Apply proper type conversions
# For example, converting 'Survived' and 'Pclass' to categorical types,
# and ensuring 'Fare' is a float (which it usually is, but good to check)
df['Survived'] = df['Survived'].astype('category')
df['Pclass'] = df['Pclass'].astype('category')

# Filling missing values in 'Age' with the median for better formatting before potential conversion
df['Age'] = df['Age'].fillna(df['Age'].median())

print("Data types after conversion:")
print(df.dtypes)
print("\n")

print("--- Step 5: Turn categorical variables into quantitative variables ---")
# Turning 'Sex' and 'Embarked' into quantitative variables using One-Hot Encoding
# Sex: male/female -> Sex_male, Sex_female (0/1)
# Embarked: C, Q, S -> Embarked_C, Embarked_Q, Embarked_S (0/1)

df_quantitative = pd.get_dummies(df, columns=['Sex', 'Embarked'])

print("First 5 rows of the transformed dataframe (Quantitative Variables):")
print(df_quantitative[['PassengerId', 'Sex_male', 'Sex_female', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].head())

# Saving the processed data
output_file = "processed_titanic_data.csv"
df_quantitative.to_csv(output_file, index=False)
print(f"\nProcessed data saved to {output_file}")
