\# Model Training Report



\## Models Trained

1\. Logistic Regression

2\. Random Forest



\## Results



\### Logistic Regression

\- Accuracy: 0.9999986

\- Precision: 1.00

\- Recall: 0.99–1.00

\- F1-score: ~1.00



\### Random Forest

\- Accuracy: 1.00

\- Precision: 1.00

\- Recall: 1.00

\- F1-score: 1.00



\## Observations

\- Both models achieved near-perfect results due to the dataset being highly imbalanced (mostly attacks, very few normal samples).

\- Random Forest slightly outperformed Logistic Regression, achieving \*\*perfect classification\*\* on this dataset.

\- For a fairer evaluation, we need to simulate \*\*zero-day scenarios\*\* by holding out one category of attack during training and testing against it.



\## Deliverables

\- Models saved in `models/`:

&nbsp; - `logistic\_regression.joblib`

&nbsp; - `random\_forest.joblib`

\- Report saved as `results/model\_report.md`



