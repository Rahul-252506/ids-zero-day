import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import os

# Load preprocessed data
print("📂 Loading preprocessed data...")
X_train, y_train = joblib.load("preprocessed/train.joblib")
X_test, y_test = joblib.load("preprocessed/test.joblib")

os.makedirs("models", exist_ok=True)

# -----------------------------
# 1️⃣ Logistic Regression
# -----------------------------
print("\n🔹 Training Logistic Regression...")
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

print("\n✅ Logistic Regression Results")
print(classification_report(y_test, y_pred_log))
print("Accuracy:", accuracy_score(y_test, y_pred_log))

joblib.dump(log_model, "models/logistic_regression.joblib")

# -----------------------------
# 2️⃣ Random Forest
# -----------------------------
print("\n🔹 Training Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print("\n✅ Random Forest Results")
print(classification_report(y_test, y_pred_rf))
print("Accuracy:", accuracy_score(y_test, y_pred_rf))

joblib.dump(rf_model, "models/random_forest.joblib")

print("\n🎯 Training complete. Models saved in models/ folder.")
