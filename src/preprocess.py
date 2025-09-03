import pandas as pd
import numpy as np
import joblib, os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load dataset
df = pd.read_csv("data/Bot_IoT_combined.csv", low_memory=False)

# Drop unnecessary cols
drop_cols = ['pkSeqID', 'stime', 'saddr', 'daddr']
df = df.drop(columns=drop_cols, errors='ignore')

# Target column
y = df['attack']
X = df.drop(columns=['attack'])

# Identify numeric/categorical cols
num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = [c for c in X.columns if c not in num_cols]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Preprocessing pipeline
preproc = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
])

X_train_t = preproc.fit_transform(X_train)
X_test_t = preproc.transform(X_test)

# Save
os.makedirs("preprocessed", exist_ok=True)
joblib.dump(preproc, "preprocessed/preprocessor.joblib")
joblib.dump((X_train_t, y_train), "preprocessed/train.joblib")
joblib.dump((X_test_t, y_test), "preprocessed/test.joblib")

print("✅ Preprocessing done. Files saved in preprocessed/")
