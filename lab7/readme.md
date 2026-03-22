# Feature Selection using Breast Cancer Dataset

## Overview

This project demonstrates how feature selection techniques can improve the performance and efficiency of machine learning models. Using the Breast Cancer Wisconsin dataset from scikit-learn, multiple feature selection methods are applied and their impact on model accuracy and complexity is analyzed.

---

## Objective

- Build a baseline Logistic Regression model using all features
- Apply and compare the following feature selection techniques:
  - Filter Method (SelectKBest)
  - Wrapper Method (Recursive Feature Elimination — RFE)
  - Embedded Method (L1 Regularization)
  - Embedded Method (Tree-Based Selection)
- Analyze the trade-off between number of features and model performance

---

## Dataset

| Property | Value |
|----------|-------|
| Name | Breast Cancer Wisconsin Dataset |
| Source | scikit-learn |
| Samples | 569 |
| Features | 30 |
| Target Classes | 0 — Malignant, 1 — Benign |

---

## Technologies Used

- Python
- NumPy
- Pandas
- scikit-learn
- Matplotlib

---

## Methodology

### 1. Data Preprocessing

- Loaded dataset using `sklearn.datasets`
- Converted data into a Pandas DataFrame
- Split data into training and testing sets
- Applied feature scaling using `StandardScaler`

### 2. Baseline Model

- **Model:** Logistic Regression
- **Features used:** All 30
- **Accuracy:** 97.37%

### 3. Feature Selection Techniques

#### Filter Method — SelectKBest

- Selected top 10 features using the ANOVA F-test
- **Accuracy:** 97.37%

#### Wrapper Method — RFE (Recursive Feature Elimination)

- Recursively eliminated less important features
- Selected 10 features
- **Accuracy:** 97.37%

#### Embedded Method — L1 Regularization

- Applied L1 penalty to remove less important features
- Reduced features to 3
- **Accuracy:** 96.49%

#### Embedded Method — Tree-Based Selection

- Used Random Forest feature importance scores
- Selected 9 features
- **Accuracy:** 97.37%

---

## Results

| Method | Features Used | Accuracy |
|--------|--------------|----------|
| Baseline | 30 | 97.37% |
| SelectKBest | 10 | 97.37% |
| RFE | 10 | 97.37% |
| L1 Regularization (C=0.01) | 3 | 96.49% |
| Tree-Based Selection | 9 | 97.37% |

---

## Key Insights

- Feature selection significantly reduces model complexity without sacrificing accuracy.
- Many of the 30 features are redundant and contribute little to predictive performance.
- SelectKBest and RFE both reduced features by 67% while maintaining full baseline accuracy.
- L1 regularization produced the most compact model (3 features) with only a marginal accuracy drop.
- Tree-based selection offered the best overall balance between performance and efficiency.

---

## Visualizations

The project includes the following plots:

- Accuracy comparison across all methods (bar chart)
- Feature count comparison across all methods
- Feature importance scores from the Random Forest model

---

## Conclusion

Feature selection is a critical preprocessing step in machine learning that improves model interpretability, reduces overfitting, and lowers computational cost. Among the methods tested, tree-based feature selection provided the best trade-off between accuracy and model simplicity, while L1 regularization delivered the most aggressive dimensionality reduction.

---

## Project Structure

```
feature-selection-project/
├── notebook.ipynb
├── README.md
├── images/
└── report.pdf
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/feature-selection-project.git
cd feature-selection-project
```

Install dependencies:

```bash
pip install numpy pandas scikit-learn matplotlib
```

Launch the notebook:

```bash
jupyter notebook
```

---

## Learning Outcomes

- Understanding and implementing multiple feature selection strategies
- Comparing filter, wrapper, and embedded methods in practice
- Analyzing the relationship between model complexity and performance
- Hands-on experience with scikit-learn's feature selection API

---

## Future Work

- Use cross-validation for more robust performance evaluation
- Test feature selection with other classifiers (SVM, Decision Trees, XGBoost)
- Apply techniques to higher-dimensional, real-world datasets
- Explore dimensionality reduction methods such as PCA for comparison

---

## Author

**Kaushal Kumar**  
CSE Student | Aspiring Data Scientist