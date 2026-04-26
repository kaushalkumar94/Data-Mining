# Lab 11 — Anomaly Detection Model Comparison

## Aim

To implement and compare three unsupervised anomaly detection algorithms — **Isolation Forest**, **One-Class SVM**, and **Local Outlier Factor (LOF)** — on a synthetic dataset, and evaluate them based on F1 Score and computation time.

---

## Theory

Anomaly detection (also called outlier detection) is the task of identifying data points that deviate significantly from the majority of the data. Unlike supervised classification, anomaly detection typically operates **without labeled training data** — the model learns what "normal" looks like and flags deviations.

### 1. Isolation Forest

Isolation Forest is an **ensemble-based** algorithm that isolates anomalies by randomly selecting a feature and then randomly selecting a split value between the max and min of that feature. Anomalies, being rare and different, require fewer splits to isolate and thus have shorter average path lengths in the isolation trees.

- **How it works:** Builds an ensemble of isolation trees; anomaly score is based on how quickly a point is isolated.
- **Key parameter:** `contamination` — the expected proportion of anomalies in the dataset.
- **Strength:** Highly scalable, works well in high-dimensional data.

### 2. One-Class SVM

One-Class SVM is a **kernel-based** method that learns a decision boundary enclosing the "normal" region of the feature space. Points outside this boundary are flagged as anomalies.

- **How it works:** Finds a hyperplane (in kernel space) that separates normal data from the origin with maximum margin.
- **Key parameter:** `nu` — an upper bound on the fraction of outliers and a lower bound on support vectors.
- **Strength:** Effective in high-dimensional spaces; works well with non-linear boundaries using RBF kernel.

### 3. Local Outlier Factor (LOF)

LOF is a **density-based** algorithm that measures the local deviation of a data point relative to its neighbours. A point with a substantially lower density than its neighbours is considered an anomaly.

- **How it works:** Computes the ratio of the average local density of a point's k-nearest neighbours to its own local density. A score > 1 indicates an outlier.
- **Key parameter:** `contamination` — proportion of anomalies; `n_neighbors` — number of nearest neighbours to consider.
- **Strength:** Detects local anomalies that global methods may miss; does not assume a global model.

---

## Dataset

A **synthetic dataset** was constructed using `make_blobs` from scikit-learn:

| Component        | Count | Description                              |
|-----------------|-------|------------------------------------------|
| Normal samples   | 300   | 2 clusters, `cluster_std=0.8`            |
| Injected outliers| 30    | Uniform random in range \[-8, 8\]        |
| **Total**        | **330** | Label: 0 = Normal, 1 = Anomaly         |

All features were standardized using `StandardScaler` before model training. A fixed `random_seed=42` was used for reproducibility.

---

## What Was Built

A Python notebook (`Anomaly_Detection_Model_Comparison.ipynb`) that:

1. Generates a 2D synthetic dataset with controlled outliers
2. Trains three anomaly detection models (Isolation Forest, One-Class SVM, LOF)
3. Predicts anomaly labels (converting sklearn's -1/+1 output to 0/1)
4. Evaluates using **F1 Score** (since the dataset is imbalanced — 30 anomalies vs 300 normal)
5. Records and compares **computation time** per model
6. Produces three visualizations: scatter plot, F1 comparison, and time comparison

---

## Results & Visualizations

### Scatter Plot — Isolation Forest Predictions

The scatter plot shows the 2D feature space after standardization. Blue points are predicted **Normal (0)** and Red points are predicted **Anomalies (1)**. The two clusters of normal data are clearly visible, with outliers scattered around the periphery.

![Isolation Forest Scatter Plot](lab11/screenshots/scatter_plot.png)

> Isolation Forest correctly identifies the scattered outlier points while keeping the two dense clusters intact.

---

### F1 Score Comparison

F1 Score is used as the primary evaluation metric because the dataset is **class-imbalanced** (only ~9% anomalies). It balances Precision and Recall:

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

![F1 Score Comparison](lab11/screenshots/f1_score.png)

| Model            | F1 Score |
|-----------------|----------|
| Isolation Forest | **0.76** |
| One-Class SVM    | 0.65     |
| LOF              | **0.76** |

**Isolation Forest** and **LOF** tie for the best F1 Score of **0.76**, while One-Class SVM lags at **0.65**. One-Class SVM's lower performance may be due to sensitivity to the `nu` parameter and the shape of the data distribution.

---

### Computation Time Comparison

![Computation Time Comparison](lab11/screenshots/time_comparison.png)

| Model            | Time (seconds) |
|-----------------|----------------|
| Isolation Forest | 0.5108         |
| One-Class SVM    | 0.0132         |
| LOF              | 0.0133         |

**Isolation Forest** is significantly slower (~0.51s) compared to One-Class SVM and LOF (~0.013s each). This is because Isolation Forest builds an **ensemble of 100 trees** (by default), which adds computation overhead. One-Class SVM and LOF are both fast on small datasets.

---

## How to Run

```bash
# Install dependencies
pip install scikit-learn numpy matplotlib

# Open and run the notebook
jupyter notebook Anomaly_Detection_Model_Comparison.ipynb
```

Or run cells sequentially — no external dataset is needed, the synthetic data is generated inside the notebook.

---

## Key Takeaways

- **Best accuracy:** Isolation Forest and LOF both achieve F1 = 0.76, outperforming One-Class SVM.
- **Fastest models:** One-Class SVM and LOF are ~40× faster than Isolation Forest on this dataset size.
- **Best overall choice:** LOF offers the best trade-off — high F1 and low computation time.
- **One-Class SVM** may improve with kernel tuning (`rbf`, `gamma` adjustment) but is harder to configure.
- F1 Score is preferred over accuracy for anomaly detection due to class imbalance.
- All three models are **unsupervised** — they require no labels during training, only the contamination ratio as a hint.

---

## Files

```
Lab11-Anomaly-Detection/
├── Anomaly_Detection_Model_Comparison.ipynb   # Main experiment notebook
├── scatter_plot.png                           # Isolation Forest predictions
├── f1_score.png                               # F1 Score bar chart
├── time_comparison.png                        # Computation time bar chart
└── README.md                                  # This file
```

---

*Lab 11 | Data Mining | Anomaly Detection*
