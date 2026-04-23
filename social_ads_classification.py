import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Create a synthetic Social Network Ads dataset
np.random.seed(42)
n_samples = 400
ages = np.random.randint(18, 60, n_samples)
salaries = np.random.randint(15000, 150000, n_samples)

# Simple logic for 'Purchased': higher age and salary increase purchase probability
# We'll use a sigmoid-like logic or simple thresholds for the synthetic labels
z = 0.1 * (ages - 35) + 0.00005 * (salaries - 70000)
probabilities = 1 / (1 + np.exp(-z))
purchased = (probabilities > np.random.rand(n_samples)).astype(int)

data = pd.DataFrame({
    'User ID': range(1001, 1001 + n_samples),
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'Age': ages,
    'EstimatedSalary': salaries,
    'Purchased': purchased
})

print("--- Step 1: Data Exploration (Synthetic Dataset) ---")
print(f"Dataset Dimensions: {data.shape}")
print(data.head())

# Features: Age and EstimatedSalary (Columns 2 and 3)
# Target: Purchased (Column 4)
X = data.iloc[:, [2, 3]].values
y = data.iloc[:, 4].values

print("\n--- Step 2: Training and Testing Split ---")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

print("\n--- Step 3: Feature Scaling ---")
# Scaling is crucial for Logistic Regression when features have different units (Age vs Salary)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print("Features have been standardized.")

print("\n--- Step 4: Model Training (Logistic Regression) ---")
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

print("\n--- Step 5: Predictions and Evaluation ---")
y_pred = classifier.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Performance Metrics
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\nAccuracy Score: {accuracy:.4f}")
print("\nClassification Report:")
print(report)

# Visualizing results (Logic for Confusion Matrix heatmap)
import seaborn as sns
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix for Social Network Ads')
plt.savefig('confusion_matrix_ads.png')
print("\nConfusion matrix heatmap saved as 'confusion_matrix_ads.png'")
