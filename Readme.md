# Data Mining Lab Work

A comprehensive collection of hands-on data mining labs covering core concepts from Python fundamentals to machine learning — implemented using Python, Jupyter Notebooks, and popular data science libraries.

---

## Repository Structure

```
Data-Mining/
├── Lab1/
│   └── IntroductionToPython.py
├── lab2/
│   ├── data used/
│   └── file_handling.ipynb
├── lab3/
│   ├── analysis.ipynb
│   ├── data generation.ipynb
│   └── readme.md
├── lab4/
│   ├── average_monthly_temperature.csv
│   └── lab4.ipynb
├── lab5/
│   ├── lab5.ipynb
│   ├── student_marks_dataset.csv
│   └── readme.md
├── lab6/
│   ├── Apriori algo.py
│   ├── Apriori from Scratch.ipynb
│   ├── Apriori on DS.ipynb
│   ├── Groceries_dataset.csv
│   └── readme.md
├── lab7/
│   ├── dataset.py
│   ├── feature selection.ipynb
│   └── readme.md
├── lab8/
│   ├── ML_Algorithms.ipynb
│   └── readme.md
└── lab9/
    ├── regression_lab.py
    ├── README.md
    └── outputs/
        ├── housing_model_comparison.png
        ├── diabetes_model_comparison.png
        ├── cross_dataset_comparison.png
        └── metrics_heatmap.png
```

---

## Labs Overview

### Lab 1 — Introduction to Python
**File:** `Lab1/IntroductionToPython.py`

An introductory lab covering the basics of Python programming as a foundation for data mining tasks. Topics include variables, data types, control flow, functions, and basic I/O operations.

---

### Lab 2 — Data Input and Data Representation
**Files:** `lab2/file_handling.ipynb`, `lab2/data used/`

Explores various ways to read, write, and represent data in Python. Covers file handling using JSON and other formats, and demonstrates how raw data can be loaded and structured for analysis.

---

### Lab 3 — Financial Data Preprocessing and Integration
**Files:** `lab3/data generation.ipynb`, `lab3/analysis.ipynb`

Focuses on preprocessing techniques applied to financial data. Covers data generation, cleaning, handling missing values, data integration, and preparing datasets for further analysis.

---

### Lab 4 — Visualization of Monthly Temperature Trends using Matplotlib
**Files:** `lab4/lab4.ipynb`, `lab4/average_monthly_temperature.csv`

Demonstrates data visualization using `matplotlib`. Uses a real-world monthly temperature dataset to create line plots, bar graphs, and trend analyses that help interpret temporal data patterns.

---

### Lab 5 — Comparative Data Visualization Using Multiple Charts
**Files:** `lab5/lab5.ipynb`, `lab5/student_marks_dataset.csv`

Extends visualization concepts by applying multiple chart types (bar, pie, scatter, histogram) on a student marks dataset. The goal is to compare different visualization strategies for the same underlying data.

---

### Lab 6 — Implementation and Understanding of Apriori Algorithm
**Files:** `lab6/Apriori algo.py`, `lab6/Apriori from Scratch.ipynb`, `lab6/Apriori on DS.ipynb`, `lab6/Groceries_dataset.csv`

A deep dive into association rule mining using the **Apriori Algorithm**. Includes:
- A from-scratch implementation to build intuition
- Application on a real Groceries dataset
- Analysis of support, confidence, and lift metrics

---

### Lab 7 — Machine Learning on the Breast Cancer Dataset
**Files:** `lab7/dataset.py`, `lab7/feature selection.ipynb`

Applies machine learning models to the **Breast Cancer dataset**. Covers feature selection techniques, model training, and evaluation strategies to understand and improve classification performance.

---

### Lab 8 — Classification Algorithms Comparison
**Files:** `lab8/dataset.py`, `lab8/readme.md`

A comprehensive comparison of **11 classification algorithms** applied to the Iris and Breast Cancer datasets. Covers a wide range of model families — from simple probabilistic models to ensemble methods and neural networks — evaluated across Accuracy, Precision, Recall, F1 Score, and training/prediction time.

Algorithms compared:
- Naive Bayes, Logistic Regression, SVM, Decision Tree, KNN, Perceptron
- Random Forest, Gradient Boosting, AdaBoost, Extra Trees, MLP Neural Net

Key findings: Naive Bayes, SVM, and Decision Tree achieve the highest accuracy on Iris (0.9667). Ensemble methods offer robustness at the cost of training time. Perceptron struggles on non-linearly separable classes.

---

### Lab 9 — Regression Algorithms Comparison
**Files:** `lab9/regression_lab.py`, `lab9/README.md`, `lab9/outputs/`

A comprehensive comparison of **10 regression algorithms** applied to the California Housing and Diabetes datasets. Covers parametric, regularized, ensemble, kernel-based, and instance-based regressors, evaluated using MAE, MSE, RMSE, and R² Score.

Algorithms compared:
- Linear Regression, Ridge, Lasso, Elastic Net
- Decision Tree, Random Forest, Gradient Boosting, AdaBoost
- SVR (RBF kernel), KNN Regressor

Key findings: Gradient Boosting achieved the best R² on both datasets (0.8624 on Housing, 0.5062 on Diabetes). Random Forest is the best accuracy/speed trade-off. SVR and KNN are not suitable for large datasets.

---

## Technologies Used

| Tool / Library | Purpose |
|----------------|---------|
| Python 3.x | Core programming language |
| Jupyter Notebook | Interactive lab environment |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Enhanced statistical visualizations |
| Scikit-learn | Machine learning models |
| mlxtend | Apriori algorithm implementation |

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaushalkumar94/Data-Mining.git
   cd Data-Mining
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn mlxtend jupyter
   ```

3. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

4. Navigate to any lab folder and open the `.ipynb` file to get started. For `.py` scripts (Lab 8, Lab 9), run them directly with `python <filename>.py`.

---

## Author

**Kaushal Kumar**
GitHub: [@kaushalkumar94](https://github.com/kaushalkumar94)
Leetcode: [leetcode grind here](https://leetcode.com/u/kaushal5354/)

---

> *These labs were completed as part of a Data Mining course curriculum.*
