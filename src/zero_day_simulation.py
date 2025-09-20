import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder

# ------------------------------------------------------------
# 1️⃣ Load the full combined dataset
# ------------------------------------------------------------
df = pd.read_csv("data/Bot_IoT_combined.csv", low_memory=False)

# 2️⃣ Choose the zero-day category to hold out
zero_day_category = "Recon"   # change to DDoS, Theft, etc. if needed

# ------------------------------------------------------------
# 3️⃣ Split into training and zero-day sets
# ------------------------------------------------------------
attack_df = df[df['attack'] == 1]
normal_df = df[df['attack'] == 0]

# Attacks we will train on (exclude the chosen zero-day category)
seen_attacks = attack_df[attack_df['category'] != zero_day_category]
zero_day_attacks = attack_df[attack_df['category'] == zero_day_category]

# Training = normal traffic + seen attacks
# Testing  = normal traffic + held-out zero-day attacks
train_df = pd.concat([seen_attacks, normal_df], ignore_index=True)
test_df  = pd.concat([zero_day_attacks, normal_df], ignore_index=True)

print(f"Training set size: {train_df.shape},  Test set size: {test_df.shape}")

# ------------------------------------------------------------
# 4️⃣ Drop high-cardinality columns
# ------------------------------------------------------------
drop_cols = ['pkSeqID', 'stime', 'saddr', 'daddr', 'sport', 'dport']
X_train = train_df.drop(columns=drop_cols + ['attack'])
y_train = train_df['attack']
X_test  = test_df.drop(columns=drop_cols + ['attack'])
y_test  = test_df['attack']

# ------------------------------------------------------------
# 5️⃣ Label-encode categorical columns
#     Fit on combined train + test to handle unseen categories
# ------------------------------------------------------------
cat_cols = X_train.select_dtypes(exclude=['number']).columns
for col in cat_cols:
    le = LabelEncoder()
    le.fit(pd.concat([X_train[col].astype(str), X_test[col].astype(str)]))
    X_train[col] = le.transform(X_train[col].astype(str))
    X_test[col]  = le.transform(X_test[col].astype(str))

# ------------------------------------------------------------
# 6️⃣ Train Random Forest
# ------------------------------------------------------------
print(f"\nTraining Random Forest (zero-day category = {zero_day_category}) ...")
rf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)
rf.fit(X_train, y_train)

# ------------------------------------------------------------
# 7️⃣ Evaluate on the held-out zero-day category
# ------------------------------------------------------------
y_pred = rf.predict(X_test)
print("\n=== Zero-Day Simulation Results ===")
print(f"Held-out category: {zero_day_category}")
print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1]))

# ------------------------------------------------------------
# 8️⃣ Save the trained model
# ------------------------------------------------------------
model_path = f"models/random_forest_zero_day_{zero_day_category}.joblib"
joblib.dump(rf, model_path)
print(f"\nModel saved to {model_path}")
