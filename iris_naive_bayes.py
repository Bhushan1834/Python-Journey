import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt

# Load the Iris dataset
try:
    df = sns.load_dataset('iris')
    print("Iris dataset loaded from Seaborn.\n")
except:
    url = "https://raw.githubusercontent.com/uiuc-cse/dataset-iris/master/iris.csv"
    df = pd.read_csv(url)
    print("Iris dataset loaded from URL.\n")

print("--- Step 1: Data Preparation ---")
print(df.head())

# Features and Target
X = df.drop('species', axis=1)
y = df['species']

# Split into Training and Testing sets (30% test size)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

print("\n--- Step 2: Model Training (Naive Bayes) ---")
# Using Gaussian Naive Bayes because the features are continuous values
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

print("\n--- Step 3: Predictions and Evaluation ---")
y_pred = nb_classifier.predict(X_test)

# Evaluation Metrics
print(f"Accuracy Score: {accuracy_score(y_test, y_pred) * 100:.2f}%")

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualizing the Confusion Matrix
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=df['species'].unique(), yticklabels=df['species'].unique())
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Naive Bayes Confusion Matrix - Iris Dataset')
plt.savefig('iris_nb_confusion_matrix.png')
print("\nConfusion matrix saved as 'iris_nb_confusion_matrix.png'")
