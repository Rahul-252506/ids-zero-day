# Model Evaluation Report

## Overview
This evaluation uses the preprocessed Bot-IoT dataset and the trained
Logistic Regression and Random Forest models.  
Test set size: **733,705 samples** (95 normal, 733,610 attack).

---

## Logistic Regression
- **Accuracy:** **1.00**
- **Precision:** 1.00
- **Recall:** Normal 0.99 / Attack 1.00
- **F1-score:** ~1.00
- **ROC-AUC:** 0.99999994

**Observations**
- Very high detection performance.
- Slightly lower recall for the normal class due to heavy class imbalance.

---

## Random Forest
- **Accuracy:** **1.00**
- **Precision:** 1.00
- **Recall:** 1.00 (both classes)
- **F1-score:** 1.00
- **ROC-AUC:** 1.00

**Observations**
- Perfect classification on the test set.
- Handles class imbalance well and matches or exceeds Logistic Regression.

---

## Confusion Matrix
A confusion matrix plot has been saved to: results/confusion_matrix.png


---

## Notes & Next Steps
- The dataset is highly imbalanced (only **95 normal** samples).
- These near-perfect metrics are expected because of the imbalance.
- For realistic intrusion-detection evaluation:
  - Simulate a **zero-day scenario** by holding out one attack category.
  - Explore data balancing or anomaly-detection methods.

---

**Prepared by:** Muthu Venkatesh M
**Date:** *(16-09-2025)*


