# Financial Data Preprocessing Program

## Data Generation

The datasets used in this program were generated using the notebook **`data_generation.ipynb`**. This notebook creates messy, randomly generated data to simulate real-world data quality issues.

**Generated files:**
- `transactions_dirty.csv`
- `customers_dirty.json`

---

## 1. Objective

The objective of this program is to preprocess financial datasets by performing:

- Data cleaning
- Data transformation
- Data integration

The final goal is to prepare a unified dataset suitable for machine learning tasks such as credit risk analysis or customer segmentation.

---

## 2. Datasets Used

### 2.1 transactions.csv

**Contains:**
- `CustomerID`
- `Monthly_Spend`
- `Account_Balance`
- `Trans_Count`

**Issues identified:**
- Missing values in `Monthly_Spend`
- Missing values in `Account_Balance`
- Duplicate transaction records

### 2.2 customers.json

**Contains:**
- `CustomerID`
- `Age`
- `Gender`
- `Credit_Score`
- `Region`

**Issues identified:**
- Missing `Age` values
- Invalid `Age` values (negative and >100)
- Inconsistent `Gender` values (M, m, Mle, FEMALE, etc.)
- Inconsistent `Region` formatting (south, SOUTH, East, etc.)

---

## 3. Data Cleaning

### 3.1 Cleaning Transactions Dataset

- **Duplicate removal:** Duplicate transaction records were removed using `drop_duplicates()`
- **Missing value imputation:** Missing numerical values were handled using median imputation:
  - `Monthly_Spend` → filled with median
  - `Account_Balance` → filled with median
- **Rationale:** Median was used because financial data may contain outliers

**After cleaning:**
- No duplicate records
- No missing values

### 3.2 Cleaning Customers Dataset

- **Invalid Age handling:** Invalid `Age` values (<0 and >100) were replaced with null values
- **Missing Age imputation:** Missing `Age` values were filled using the median `Age`
- **Gender standardization:** 
  - All values converted to lowercase
  - M, m, Mle → `male`
  - F, FEMALE → `female`
- **Region standardization:**
  - Converted to lowercase
  - Capitalized properly
  - Final values: `North`, `South`, `East`, `West`

**After cleaning:**
- No missing values
- No invalid values
- Consistent categorical formatting

---

## 4. Data Transformation

### 4.1 Scaling Numerical Features

`Monthly_Spend` and `Account_Balance` were scaled using **MinMaxScaler**.

**Purpose:**
- To normalize data between 0 and 1
- To prevent large-value features from dominating machine learning models

**After scaling:**
- Minimum value = 0
- Maximum value = 1

### 4.2 Encoding Categorical Feature

`Gender` column was encoded into numeric form:
- `male` → 1
- `female` → 0

**Rationale:** Machine learning algorithms require numerical input.

---

## 5. Data Integration

The cleaned and transformed datasets were merged using:
- **Common key:** `CustomerID`
- **Join type:** Inner join (keeps only matching records)

**The result is a unified dataset containing:**
- `CustomerID`
- `Monthly_Spend`
- `Account_Balance`
- `Trans_Count`
- `Age`
- `Gender` (encoded)
- `Credit_Score`
- `Region`

---

## 6. Final Output

**The final merged dataset:**
- Contains no missing values
- Contains no duplicate records
- Has standardized categorical data
- Has scaled numerical features
- Is ready for machine learning applications

**Output file:** `final_merged_dataset.csv`

---

## Summary

This preprocessing pipeline successfully transforms messy, real-world-like financial data into a clean, standardized format suitable for machine learning applications such as credit risk modeling and customer segmentation analysis.
