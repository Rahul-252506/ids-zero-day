import os, glob, sys
import pandas as pd

CANDIDATE_LABELS = ['label','attack','attack_type','class','category','Category','Label']

def find_label_col(df):
    for c in CANDIDATE_LABELS:
        if c in df.columns:
            return c
    for c in df.select_dtypes(include=['object','category']).columns:
        if df[c].nunique() < 200:
            return c
    return None

def analyze(path):
    try:
        df = pd.read_csv(path, low_memory=False)
    except Exception as e:
        print(f"SKIP {path}: {e}")
        return
    label = find_label_col(df)
    print("="*80)
    print(f"File: {path}")
    print(f"Rows: {len(df):,}  Columns: {df.shape[1]}")
    print("Top columns:", list(df.columns[:10]))
    if label:
        print(f"Detected label column: {label}")
        print(df[label].value_counts(dropna=False).head(40))
    else:
        print("No label column detected automatically.")
    print("Missing (top 10):")
    print(df.isnull().sum().sort_values(ascending=False).head(10))
    print()

if __name__ == '__main__':
    data_dir = sys.argv[1] if len(sys.argv)>1 else 'data'
    for f in glob.glob(os.path.join(data_dir,'*.csv')):
        analyze(f)
