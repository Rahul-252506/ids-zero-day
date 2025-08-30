\# Data Inventory Report — Bot-IoT (Reduced Kaggle Version)



\## Dataset Overview

\- Total files: 4 (reduced\_data\_1.csv … reduced\_data\_4.csv)

\- Each file has 46 columns.

\- Total rows:

&nbsp; - reduced\_data\_1.csv: 1,000,000

&nbsp; - reduced\_data\_2.csv: 1,000,000

&nbsp; - reduced\_data\_3.csv: 1,000,000

&nbsp; - reduced\_data\_4.csv: 668,522



\## Label Column

\- Detected: `attack`

\- Distribution:

&nbsp; - reduced\_data\_1.csv: 1,000,000 attack

&nbsp; - reduced\_data\_2.csv: 1,000,000 attack

&nbsp; - reduced\_data\_3.csv: 1,000,000 attack

&nbsp; - reduced\_data\_4.csv: 668,045 attack, 477 normal



\## Missing Values

\- None detected (all major columns have 0 missing values).



\## Columns to Drop (for preprocessing)

\- `pkSeqID` (just an index)

\- `stime` (timestamp, not useful directly)

\- `saddr`, `daddr` (IP addresses, not generalizable)



\## Recommendation for Zero-Day Holdout

\- Currently, all files are dominated by attack traffic, with only 477 normal rows in file 4.  

\- Recommendation: \*\*merge all 4 files into one dataset\*\* and then decide on an attack type to hold out for the zero-day scenario.



