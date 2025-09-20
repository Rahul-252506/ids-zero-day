# Zero-Day Simulation Report

## Objective
Evaluate the ability of a Random Forest intrusion detection model to
detect **unseen attacks** by holding out attack categories
(**DoS, DDoS, Theft, Recon**) during training.

---

## Zero-Day Simulation: DoS
**Held-out category:** DoS  

- **Training set size:** 2,018,262 rows  
- **Test set size:** 1,650,737 rows  

**Results:**  
| Metric | Normal (0) | Attack (1) |
|--------|------------|------------|
| Precision | 0.99 | 1.00 |
| Recall    | 1.00 | 1.00 |
| F1-score  | 0.99 | 1.00 |

- **Overall Accuracy:** 1.00  
- **ROC-AUC:** 1.0  

📌 **Notes:**  
- The model generalized strongly to DoS.  
- Slight imbalance issues with normal traffic recall.  

---

## Zero-Day Simulation: DDoS
**Held-out category:** DDoS  

**Results:**  
| Metric | Normal (0) | Attack (1) |
|--------|------------|------------|
| Precision | 1.00 | 1.00 |
| Recall    | 1.00 | 1.00 |
| F1-score  | 1.00 | 1.00 |

- **Overall Accuracy:** 1.00  
- **ROC-AUC:** 1.0  

📌 **Notes:**  
- Perfect metrics, but dataset imbalance may inflate results.  
- Still indicates strong resilience to unseen DDoS attacks.  

---

## Zero-Day Simulation: Theft
**Held-out category:** Theft  

- **Training set size:** 3,668,443 rows  
- **Test set size:** 556 rows  

**Results:**  
| Metric | Normal (0) | Attack (1) |
|--------|------------|------------|
| Precision | 1.00 | 1.00 |
| Recall    | 1.00 | 1.00 |
| F1-score  | 1.00 | 1.00 |

- **Overall Accuracy:** 1.00  
- **ROC-AUC:** 1.0  

📌 **Notes:**  
- Theft had only 79 attack samples.  
- Metrics look perfect but may be misleading due to small test size.  

---

## Zero-Day Simulation: Recon
**Held-out category:** Recon  

- **Training set size:** 3,668,522 rows  
- **Test set size:** 477 rows  

**Results:**  
| Metric | Normal (0) |
|--------|------------|
| Precision | 1.00 |
| Recall    | 1.00 |
| F1-score  | 1.00 |

- **Overall Accuracy:** 1.00  
- **ROC-AUC:** Not Applicable (only one class present).  

📌 **Notes:**  
- Recon test set had only normal samples.  
- ROC-AUC undefined → results not reliable.  

---
