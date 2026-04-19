import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load the Boston Housing dataset from a reliable URL
# Note: sklearn's load_boston is deprecated, so we load the CSV directly.
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
data = pd.read_csv(url)

print("--- Step 1: Exploratory Data Analysis (EDA) ---")
print(f"Dataset Shape: {data.shape}")
print(data.head())
print("\nMissing values check:")
print(data.isnull().sum())

# 'medv' is our target variable (Median value of owner-occupied homes)
X = data.drop('medv', axis=1) # All features
y = data['medv']              # Target variable

print("\n--- Step 2: Training and Testing Split ---")
# Split the data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training samples: {X_train.shape[0]}, Testing samples: {X_test.shape[0]}")

print("\n--- Step 3: Model Initialization and Training ---")
lm = LinearRegression()
lm.fit(X_train, y_train)

# Print coefficients
print(f"Intercept: {lm.intercept_:.4f}")
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

print("\n--- Step 4: Predictions and Evaluation ---")
predictions = lm.predict(X_test)

# Model indicators
mae = metrics.mean_absolute_error(y_test, predictions)
mse = metrics.mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(y_test, predictions)

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-Squared (Accuracy Score): {r2:.4f}")

# Visualization: Comparison Plot
plt.figure(figsize=(10,6))
plt.scatter(y_test, predictions, edgecolors=(0, 0, 0))
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=4)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Boston Housing Prices')
plt.savefig('boston_prediction_plot.png')
print("\nPrediction plot saved as 'boston_prediction_plot.png'")

# Predicting a house price with example features
sample_data = X_test.iloc[0:1]
sample_pred = lm.predict(sample_data)
print(f"\nPredicting price for a single test sample:")
print(f"Actual: {y_test.iloc[0]}, Predicted: {sample_pred[0]:.2f}")
