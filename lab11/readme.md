# Practical 11 — Anomaly Detection Techniques: A Comparative Study

> Identifying outliers and unusual patterns using five unsupervised anomaly detection algorithms across synthetic and real-world datasets.

---

## Table of Contents

- [Objective](#objective)
- [Datasets Used](#datasets-used)
- [Preprocessing](#preprocessing)
- [Algorithms Implemented](#algorithms-implemented)
- [Results & Output](#results--output)
- [Visualizations](#visualizations)
- [Performance Comparison](#performance-comparison)
- [Observations & Analysis](#observations--analysis)
- [Conclusion](#conclusion)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)

---

## Objective

To understand how different anomaly detection techniques can be applied to datasets to identify outliers and unusual patterns, and to compare their performance across evaluation metrics, hyperparameter sensitivity, and computational efficiency.

---

## Datasets Used

### 1. Synthetic Dataset (`make_blobs` + Injected Outliers)

| Property | Value |
|---|---|
| Normal samples | 300 (2 Gaussian clusters) |
| Injected outliers | 30 (random uniform noise) |
| Total samples | 330 |
| Features | 2 |
| Contamination rate | ~9.09% |

Normal points were generated using `make_blobs` with 2 centers and `cluster_std=0.8`. Outliers were injected by sampling uniformly from `[-8, 8]` in both dimensions — simulating real-world noise that lies far from any cluster.

---

### 2. Breast Cancer Dataset (`sklearn.datasets.load_breast_cancer`)

| Property | Value |
|---|---|
| Total samples | 569 |
| Features | 30 |
| Normal class | Benign (357 samples) |
| Anomaly class | Malignant (212 samples) |
| Contamination rate | ~9% (used for model config) |
| Dimensionality reduction | PCA -> 2D (for visualization) |

Malignant cases are treated as anomalies. This reflects a realistic medical scenario where rare or dangerous cases must be flagged.

---

## Preprocessing

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Feature scaling (critical for distance/density-based methods)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dimensionality reduction for visualization (Breast Cancer only)
pca = PCA(n_components=2, random_state=42)
X_2d = pca.fit_transform(X_scaled)
```

**Why StandardScaler?**
Algorithms like LOF, One-Class SVM, and Elliptic Envelope compute distances or densities. Without scaling, features with larger numerical ranges dominate and produce biased results.

**Why PCA for Breast Cancer?**
The dataset has 30 features. PCA reduces it to 2 principal components for scatter plot visualization while retaining maximum variance.

---

## Algorithms Implemented

| # | Algorithm | Type | Key Parameters |
|---|---|---|---|
| 1 | **Isolation Forest** | Ensemble / Tree-based | `contamination=0.09` |
| 2 | **One-Class SVM** | Kernel-based | `nu=0.09, kernel='rbf'` |
| 3 | **Local Outlier Factor (LOF)** | Density-based | `n_neighbors=20, contamination=0.09` |
| 4 | **Elliptic Envelope** | Statistical | `contamination=0.09` |
| 5 | **DBSCAN** | Clustering / Noise detection | `eps=0.5, min_samples=5` |

All methods output binary labels: `0 = normal`, `1 = anomaly`.  
DBSCAN's native `-1` (noise) label is mapped to `1` (anomaly).

---

## Results & Output

### Terminal Output

```
============================================================
ANOMALY DETECTION — METRICS REPORT
============================================================

------------------------------------------------------------
Dataset: Synthetic (blobs + injected outliers)
Method                  Precision   Recall       F1   Time(s)
------------------------------------------------------------
Isolation Forest            0.900    0.900    0.900    0.2132
One-Class SVM               0.724    0.700    0.712    0.0019
LOF                         0.833    0.833    0.833    0.0028
Elliptic Envelope           0.833    0.833    0.833    0.0980
DBSCAN                      1.000    0.767    0.868    0.0036

------------------------------------------------------------
Dataset: Breast Cancer (malignant=anomaly)
Method                  Precision   Recall       F1   Time(s)
------------------------------------------------------------
Isolation Forest            0.635    0.156    0.250    0.1460
One-Class SVM               0.547    0.137    0.219    0.0054
LOF                         0.462    0.113    0.182    0.2752
Elliptic Envelope           0.865    0.212    0.341    0.9241
DBSCAN                      0.373    1.000    0.543    0.0027

============================================================
Best on Synthetic:     Isolation Forest (F1=0.900)
Best on Breast Cancer: DBSCAN  (F1=0.543)
============================================================
```

---

### Metric Tables

#### Synthetic Dataset

| Method | Precision | Recall | F1-Score | Time (s) |
|---|---|---|---|---|
| **Isolation Forest** | **0.900** | **0.900** | **0.900** | 0.2132 |
| One-Class SVM | 0.724 | 0.700 | 0.712 | 0.0019 |
| LOF | 0.833 | 0.833 | 0.833 | 0.0028 |
| Elliptic Envelope | 0.833 | 0.833 | 0.833 | 0.0980 |
| DBSCAN | 1.000 | 0.767 | 0.868 | 0.0036 |

#### Breast Cancer Dataset

| Method | Precision | Recall | F1-Score | Time (s) |
|---|---|---|---|---|
| Isolation Forest | 0.635 | 0.156 | 0.250 | 0.1460 |
| One-Class SVM | 0.547 | 0.137 | 0.219 | 0.0054 |
| LOF | 0.462 | 0.113 | 0.182 | 0.2752 |
| **Elliptic Envelope** | **0.865** | 0.212 | 0.341 | 0.9241 |
| **DBSCAN** | 0.373 | **1.000** | **0.543** | 0.0027 |

---

## Visualizations

![Anomaly Detection Results](screenshots/anomaly_detection.png)

### How to Read the Scatter Plots

Each scatter plot shows the detected anomalies for one method on one dataset. Points are color-coded as:

| Color | Marker | Meaning |
|---|---|---|
| Red | X | True Positive — Anomaly correctly detected |
| Orange | Triangle | False Positive — Normal point wrongly flagged |
| Blue | Circle | False Negative — Anomaly that was missed |
| Green | Circle | True Negative — Normal point correctly ignored |

**Row 1** — Synthetic dataset scatter plots (2D, original feature space after scaling)  
**Row 2** — Breast Cancer scatter plots (2D after PCA projection)  
**Rows 3-4** — Bar charts for Precision, Recall, and F1-Score on both datasets  
**Row 5** — Computation time comparison + legend + summary panel

---

## Performance Comparison

### F1-Score Summary

```
Synthetic Dataset
-----------------------------------------
Isolation Forest  ||||||||||||||||||||  0.900  Best
DBSCAN            ||||||||||||||||||||  0.868
LOF               |||||||||||||||||||   0.833
Elliptic Envelope |||||||||||||||||||   0.833
One-Class SVM     ||||||||||||||||      0.712

Breast Cancer Dataset
-----------------------------------------
DBSCAN            ||||||||||||          0.543  Best
Elliptic Envelope ||||||||              0.341
Isolation Forest  ||||||                0.250
One-Class SVM     |||||                 0.219
LOF               ||||                  0.182
```

### Computation Time

| Method | Synthetic | Breast Cancer | Verdict |
|---|---|---|---|
| One-Class SVM | 0.0019s | 0.0054s | Fastest |
| DBSCAN | 0.0036s | 0.0027s | Very fast |
| LOF | 0.0028s | 0.2752s | Fast on small data |
| Isolation Forest | 0.2132s | 0.1460s | Consistent |
| Elliptic Envelope | 0.0980s | 0.9241s | Slow on high-dim data |

---

## Observations & Analysis

### 1. Isolation Forest
- Achieved the **highest F1 of 0.900** on synthetic data — perfectly balanced precision and recall.
- Performed moderately on Breast Cancer (F1 = 0.250) due to the high-dimensional, overlapping feature space.
- Consistent runtime regardless of dataset size — scales well.

### 2. One-Class SVM
- Weakest performer overall on both datasets.
- Highly sensitive to `nu` and `gamma` — small changes in these parameters cause significant performance swings.
- Very fast at inference but difficult to tune without labeled validation data.

### 3. Local Outlier Factor (LOF)
- Solid on synthetic data (F1 = 0.833), identifying local density deviations well.
- Struggled on Breast Cancer — LOF is computationally O(n^2) and loses effectiveness in 30-dimensional space (curse of dimensionality).
- Best suited for low-to-medium dimensional datasets with varying cluster densities.

### 4. Elliptic Envelope
- Highest **precision on Breast Cancer (0.865)** — when it flags something, it is usually correct.
- Very low recall (0.212) — it is too conservative and misses most real anomalies.
- Assumes Gaussian distribution. Breast Cancer data is multi-modal, which violates this assumption and hurts performance.
- Slowest on high-dimensional data (0.92s on Breast Cancer) due to covariance matrix estimation.

### 5. DBSCAN
- **Perfect precision (1.000)** on synthetic data — every point it flagged was a true outlier.
- **Perfect recall (1.000)** on Breast Cancer — caught every single malignant case, but at the cost of many false positives (precision = 0.373).
- Best overall F1 on Breast Cancer (0.543) despite low precision, because recall dominates in medical contexts.
- Extremely sensitive to `eps` — requires tuning via k-distance plot for best results.

### Hyperparameter Sensitivity

| Algorithm | Sensitivity | Notes |
|---|---|---|
| Isolation Forest | Low-Medium | `contamination` must approximate true outlier ratio |
| One-Class SVM | High | Both `nu` and `gamma` need careful tuning |
| LOF | Medium | `n_neighbors` affects local vs global view |
| Elliptic Envelope | Low | Mainly sensitive to data distribution assumptions |
| DBSCAN | High | `eps` and `min_samples` are critical; use k-distance plot |

---

## Conclusion

| Criterion | Best Method |
|---|---|
| Overall accuracy (structured data) | **Isolation Forest** |
| High recall (catch all anomalies) | **DBSCAN** |
| High precision (minimize false alarms) | **DBSCAN** (synthetic) / **Elliptic Envelope** (BC) |
| Speed | **One-Class SVM** / **DBSCAN** |
| High-dimensional data | **Isolation Forest** |
| Local density anomalies | **LOF** |

**Key takeaway:** No single algorithm dominates across all conditions. The best choice depends on the data's shape, dimensionality, and the use case:

- Use **Isolation Forest** as the default — robust, scalable, and well-balanced.
- Use **DBSCAN** when anomalies naturally form noise outside dense clusters.
- Use **LOF** when you expect local outliers relative to their neighborhood.
- Use **Elliptic Envelope** only when data is known to be Gaussian and precision matters.
- Avoid **One-Class SVM** unless you have time to tune hyperparameters carefully.

In safety-critical domains (e.g., medical diagnosis), **high recall** is preferred over precision — missing an anomaly is more costly than a false alarm. In those cases, DBSCAN or a low-threshold Isolation Forest is preferred.

---

## Repository Structure

```
Practical-11-Anomaly-Detection/
|
|-- anomaly_detection.py       # Main Python script
|-- README.md                  # This file
|-- screenshots/
    |-- anomaly_detection.png  # Output visualization
```

---

## Dependencies

```
numpy
matplotlib
scikit-learn
```

Install with:

```bash
pip install numpy matplotlib scikit-learn
```

---

## How to Run

```bash
# Clone or navigate to the practical folder
cd Practical-11-Anomaly-Detection

# Run the script
python anomaly_detection.py
```

**Expected outputs:**
- `screenshots/anomaly_detection.png` — full visualization grid
- Terminal metrics report with Precision, Recall, F1, and Time for all methods

---

> **Note:** All random seeds are fixed (`random_state=42`, `np.random.seed(42)`) to ensure fully reproducible results across runs.
