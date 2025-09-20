\- \*\*Random Forest Zero-Day (DoS):\*\* Accuracy = 1.0 | ROC-AUC = 1.0 | Training set: 2,018,262 | Test set: 1,650,737

\- \*\*Random Forest Zero-Day (DDoS):\*\* Accuracy = 1.0 | ROC-AUC = 1.0 | Training set: 3,668,522 | Test set: 733,705

\- \*\*Random Forest Zero-Day (Theft):\*\* Accuracy = 1.0 | ROC-AUC = 1.0 | ⚠️ Very few samples (79 attacks) → results may be over-optimistic

\- \*\*Random Forest Zero-Day (Recon):\*\* Accuracy = 1.0 | ROC-AUC = N/A | ⚠️ Only one class (normal) in test set → results not reliable

| Zero-Day Category | Training Samples | Test Samples | Accuracy | ROC-AUC | Notes |

|------------------|-----------------|--------------|----------|---------|-------|

| DoS              | 2,018,262       | 1,650,737    | 1.0      | 1.0     | - |

| DDoS             | 3,668,522       | 733,705      | 1.0      | 1.0     | - |

| Theft            | 3,668,443       | 556          | 1.0      | 1.0     | ⚠️ Very few attacks (79) |

| Recon            | 3,668,522       | 477          | 1.0      | N/A     | ⚠️ Only normal samples in test set |



