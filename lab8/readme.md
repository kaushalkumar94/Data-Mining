# Lab 8 — Classification Algorithms Comparison

> **Course:** Data Mining Lab
> **Datasets:** Iris | Breast Cancer (scikit-learn built-in)
> **Algorithms:** 11 | **Metrics:** Accuracy, Precision, Recall, F1 Score

---

## Table of Contents

1. [Aim](#aim)
2. [Theory](#theory)
3. [Algorithms Used](#algorithms-used)
4. [Datasets](#datasets)
5. [Prerequisites](#prerequisites)
6. [Project Structure](#project-structure)
7. [How to Run](#how-to-run)
8. [Results](#results)
9. [Visualisations](#visualisations)
10. [Conclusion](#conclusion)

---

## Aim

To study and compare the performance of various classification algorithms on standard datasets by implementing eleven classification techniques on the Iris and Breast Cancer datasets, evaluating them using Accuracy, Precision, Recall, and F1 Score, in order to identify which algorithms provide the best predictive performance and computational efficiency.

---

## Theory

Classification is a supervised machine learning technique used to predict a discrete categorical label based on input features. The models learn decision boundaries from training data and generalize to unseen samples.

Key concepts covered in this practical:

- **Probabilistic Models** — Using probability distributions to make predictions (Naive Bayes, Logistic Regression)
- **Kernel Methods** — Mapping data to higher dimensions to find optimal separating hyperplanes (SVM)
- **Tree-based Models** — Splitting data recursively based on feature thresholds (Decision Tree)
- **Ensemble Learning** — Combining multiple weak learners for a stronger model (Random Forest, Gradient Boosting, AdaBoost, Extra Trees)
- **Instance-based Learning** — Predicting based on nearest stored training examples (KNN)
- **Neural Networks** — Multi-layer perceptrons learning non-linear patterns (MLP)
- **Feature Scaling** — Standardizing features for distance-based and gradient-based algorithms

---

## Algorithms Used

| # | Algorithm | Type | Notes |
|---|---|---|---|
| 1 | Naive Bayes | Probabilistic | Assumes feature independence |
| 2 | Logistic Regression | Linear | `max_iter=1000` |
| 3 | SVM | Kernel-based | RBF kernel |
| 4 | Decision Tree | Tree-based | Prone to overfitting alone |
| 5 | KNN | Instance-based | k=5 neighbors |
| 6 | Perceptron | Linear | `max_iter=1000` |
| 7 | Random Forest | Ensemble (Bagging) | 100 estimators |
| 8 | Gradient Boosting | Ensemble (Boosting) | 100 estimators |
| 9 | AdaBoost | Ensemble (Boosting) | 100 estimators |
| 10 | Extra Trees | Ensemble (Bagging) | 100 estimators |
| 11 | MLP Neural Net | Neural Network | `max_iter=1000` |

---

## Datasets

### Iris Dataset
| Property | Value |
|---|---|
| Source | `sklearn.datasets.load_iris` |
| Samples | 150 |
| Features | 4 (sepal length, sepal width, petal length, petal width) |
| Classes | 3 (Setosa, Versicolor, Virginica) |
| Nature | Small, well-separated, classic benchmark |

### Breast Cancer Dataset
| Property | Value |
|---|---|
| Source | `sklearn.datasets.load_breast_cancer` |
| Samples | 569 |
| Features | 30 (radius, texture, perimeter, area, etc.) |
| Classes | 2 (Malignant, Benign) |
| Nature | Binary classification, medical domain |

---

## Prerequisites

Make sure the following libraries are installed before running the code.

```bash
pip install scikit-learn matplotlib numpy pandas seaborn
```

| Library | Version | Purpose |
|---|---|---|
| scikit-learn | ≥ 1.0 | Datasets, models, metrics |
| numpy | ≥ 1.21 | Numerical operations |
| pandas | ≥ 1.3 | Results table formatting |
| matplotlib | ≥ 3.4 | Visualisations |
| seaborn | ≥ 0.11 | Enhanced plots |

---

## Project Structure

```
lab8/
│
├── dataset.py              ← Main Python script
└── README.md               ← This file
```

---

## How to Run

**Step 1 — Navigate to the lab folder**
```bash
cd lab8
```

**Step 2 — Install dependencies**
```bash
pip install scikit-learn matplotlib numpy pandas seaborn
```

**Step 3 — Run the script**
```bash
python dataset.py
```

**Step 4 — View outputs**

The script will:
- Load and preprocess both datasets (80/20 train-test split, StandardScaler)
- Train all 11 classifiers and print a metrics table
- Display bar charts comparing Accuracy and F1 Score across models

---

## Results

### Iris Dataset

| Model | Accuracy | Precision | Recall | F1 Score | Train Time (ms) | Predict Time (ms) |
|---|---|---|---|---|---|---|
| Naive Bayes | 0.9667 | 0.9697 | 0.9667 | 0.9666 | 15.18 | 1.24 |
| Logistic Regression | 0.9333 | 0.9333 | 0.9333 | 0.9333 | 6.39 | 0.00 |
| SVM | 0.9667 | 0.9697 | 0.9667 | 0.9666 | 3.00 | 1.00 |
| Decision Tree | 0.9667 | 0.9697 | 0.9667 | 0.9666 | 3.00 | 0.00 |
| KNN | 0.9333 | 0.9444 | 0.9333 | 0.9327 | 0.00 | 0.00 |
| Perceptron | 0.8000 | 0.8586 | 0.8000 | 0.7746 | 6.00 | 0.90 |
| Random Forest | 0.9333 | 0.9333 | 0.9333 | 0.9333 | 312.31 | 13.40 |
| Gradient Boosting | 0.9667 | 0.9697 | 0.9667 | 0.9666 | 616.21 | 0.00 |
| AdaBoost | 0.9333 | 0.9333 | 0.9333 | 0.9333 | 332.18 | 30.91 |
| Extra Trees | 0.9333 | 0.9333 | 0.9333 | 0.9333 | 231.52 | 20.34 |
| MLP Neural Net | 0.9667 | 0.9697 | 0.9667 | 0.9666 | 587.69 | 0.00 |

> Metrics for Iris use **macro averaging** (multi-class). For Breast Cancer, **binary averaging** is used.

---

## Visualisations

Bar charts comparing **Accuracy** and **F1 Score** across all 11 models are generated for both datasets:

- **Iris Dataset Model Comparison** — `plot_results(iris_results, "Iris Dataset Model Comparison")`
- **Breast Cancer Dataset Model Comparison** — `plot_results(cancer_results, "Breast Cancer Dataset Model Comparison")`

---

## Conclusion

- **Naive Bayes, SVM, Decision Tree, Gradient Boosting, and MLP** all achieved the highest accuracy (0.9667) on the Iris dataset. For a small, well-structured dataset like Iris, many algorithms perform comparably.

- **Perceptron** performed the worst on Iris (0.80 accuracy) — it is a linear model and struggles with non-linearly separable classes.

- **Ensemble methods** (Random Forest, Gradient Boosting, AdaBoost, Extra Trees) incur significantly higher training times but do not always offer proportional accuracy gains on small datasets.

- **KNN and Logistic Regression** offer a solid accuracy-speed trade-off and are good baselines for classification tasks.

- The choice of averaging strategy (macro vs binary) meaningfully affects reported Precision, Recall, and F1 values — always match the averaging method to the problem type.

### Final Recommendation

| Use Case | Recommended Algorithm |
|---|---|
| Maximum accuracy (small dataset) | Naive Bayes / SVM / Decision Tree |
| Best accuracy / speed trade-off | Naive Bayes or SVM |
| Interpretable results | Decision Tree, Logistic Regression |
| Robust, general-purpose | Random Forest |
| Avoid for non-linear data | Perceptron |

---

*Lab 8 — Data Mining Lab*
