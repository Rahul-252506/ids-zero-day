import joblib, numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# === Load data & models ===
X_test, y_test = joblib.load("preprocessed/test.joblib")
log_reg = joblib.load("models/logistic_regression.joblib")
rf      = joblib.load("models/random_forest.joblib")

# === Evaluate Logistic Regression ===
print("\n==== Logistic Regression ====")
y_pred_lr = log_reg.predict(X_test)
print(classification_report(y_test, y_pred_lr))
print("ROC-AUC:", roc_auc_score(y_test, log_reg.predict_proba(X_test)[:,1]))

# === Evaluate Random Forest ===
print("\n==== Random Forest ====")
y_pred_rf = rf.predict(X_test)
print(classification_report(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, rf.predict_proba(X_test)[:,1]))

# === Confusion Matrix Plot ===
cm = confusion_matrix(y_test, y_pred_rf)
plt.matshow(cm, cmap="Blues")
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.colorbar()
plt.savefig("results/confusion_matrix.png")
plt.close()
