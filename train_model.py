import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# ======================================================
# Load Dataset
# ======================================================

data = pd.read_csv("dataset/Crop_recommendation.csv")

# ======================================================
# Display Dataset
# ======================================================

print("First 5 Rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDataset Information:")
data.info()

print("\nMissing Values:")
print(data.isnull().sum())

print("\nStatistical Summary:")
print(data.describe())

print("\nCrop Counts:")
print(data['label'].value_counts())

# ======================================================
# Exploratory Data Analysis (Optional)
# Uncomment to generate graphs
# ======================================================

"""
# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    data.drop('label', axis=1).corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()

# Distribution Plots
numeric_columns = ['N','P','K','temperature','humidity','ph','rainfall']

for column in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.histplot(data[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

# Boxplots
for column in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=data[column])
    plt.title(f"Boxplot of {column}")
    plt.show()
"""

# ======================================================
# Data Preprocessing
# ======================================================

X = data.drop('label', axis=1)
y = data['label']

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nX_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)

print("\ny_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)

# ======================================================
# Feature Scaling
# ======================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nData preprocessing completed successfully!")

# ======================================================
# Machine Learning Models
# ======================================================

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Naive Bayes": GaussianNB()
}

best_model = None
best_accuracy = 0

print("\n==============================")
print("Model Accuracies")
print("==============================")

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name}: {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

print("\nBest Model Accuracy:", best_accuracy)

# ======================================================
# Classification Report
# ======================================================

predictions = best_model.predict(X_test)

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# ======================================================
# Save Model
# ======================================================

os.makedirs("model", exist_ok=True)

joblib.dump(best_model, "model/model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("\nModel and scaler saved successfully!")