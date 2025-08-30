import pandas as pd
import glob, os

# Folder where CSVs are stored
data_dir = "data"
out_file = os.path.join(data_dir, "Bot_IoT_combined.csv")

# Grab all reduced_data_*.csv files
files = sorted(glob.glob(os.path.join(data_dir, "reduced_data_*.csv")))

print("Merging files:", files)

dfs = []
for f in files:
    print("Reading:", f)
    df = pd.read_csv(f, low_memory=False)
    dfs.append(df)

# Concatenate
combined = pd.concat(dfs, ignore_index=True)
print("Final shape:", combined.shape)

# Save combined CSV
combined.to_csv(out_file, index=False)
print("Saved:", out_file)
