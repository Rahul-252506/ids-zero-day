# Zero-Day Simulation Report

## Objective
Evaluate the ability of a Random Forest intrusion detection model to
detect **unseen attacks** by holding out one attack category
(**DoS**) during training.

---

## Data Split
- **Training set size:** 2,018,262 rows  
  - Includes all normal traffic and all attack categories **except DoS**.
- **Test set size:** 1,650,737 rows  
  - Contains all normal traffic and **only DoS** attacks (zero-day scenario).

---

## Model & Configuration
- **Algorithm:** Random Forest Classifier  
- **Estimators:** 100  
- **Random State:** 42  
- **Feature Handling:**  
  - Dropped high-cardinality columns (`pkSeqID`, `stime`, `saddr`, `daddr`, `sport`, `dport`)  
  - Label-encoded remaining categorical columns.

---

## Results
| Metric | Normal (0) | Attack (1) |
|-------|-----------|-----------|
| **Precision** | 0.99 | 1.00 |
| **Recall**    | 1.00 | 1.00 |
| **F1-score**  | 0.99 | 1.00 |

- **Overall Accuracy:** **1.00**  
- **ROC-AUC:** **1.0**

---

## Observations
- The Random Forest model perfectly detected the unseen **DoS** attacks.
- Normal traffic recall was slightly lower (0.99), likely due to heavy class imbalance.
- This demonstrates strong generalization to a zero-day attack type.

---

## Next Steps
- Repeat the experiment holding out other categories (e.g., DDoS, Theft) for broader validation.
- Investigate additional techniques for handling class imbalance to maintain normal-class recall.

---

**Prepared by:** Muthu  
**Date:** 16-09-2025
