import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from feature_extraction import extract_features

# Load dataset
df = pd.read_csv("dataset.csv")

# Fix column names automatically (URL → url)
df.columns = df.columns.str.lower()

X = []
y = df['label']

print("Extracting features...")

# 🔹 IMPORTANT: WHOIS OFF for training
for url in df['url']:
    try:
        features = extract_features(url, use_whois=False)[0]
        X.append(features)
    except:
        continue

# Convert to DataFrame
X = pd.DataFrame(X)

# Align labels
y = y[:len(X)]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "phishing_model.pkl")

print("Model saved successfully!")