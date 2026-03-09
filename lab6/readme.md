# 🛒 Market Basket Analysis – Apriori Algorithm

> Discovering hidden purchasing patterns using association rule mining in Python.

---

## 📌 Overview

This project demonstrates the implementation of the **Apriori Algorithm** for **Market Basket Analysis** using Python. The goal is to discover **frequent itemsets** and generate **association rules** that reveal relationships between items purchased together.

The analysis is performed on a small transactional dataset containing food items such as cookies, chocolate, cake, burgers, and others.

---

## 🎯 Objectives

- Implement the Apriori algorithm from scratch using Python
- Identify **frequent itemsets** from a transaction dataset
- Generate **association rules** using support, confidence, and lift
- Interpret customer purchasing patterns for business decisions

---

## 🗃️ Dataset

The dataset consists of **6 transactions** containing food items:

| Transaction ID | Items                              |
|----------------|------------------------------------|
| T1             | Cookie, Chocolate, Ice Cream, Cake |
| T2             | Cookie, Chocolate, Donut           |
| T3             | Cookie, Chocolate, Cake            |
| T4             | Bread, Egg, Tomato                 |
| T5             | Pizza, Burger                      |
| T6             | Fries, Burger                      |

---

## 🧰 Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| Pandas | Data manipulation and encoding |
| Mlxtend | Apriori algorithm & association rules |
| Jupyter Notebook | Development environment |

### Installation

```bash
pip install pandas mlxtend
```

---

## ⚙️ Methodology

### 1. Data Preparation

Transactions were converted into **one-hot encoded** format using `TransactionEncoder` from `mlxtend`:

```python
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

dataset = [
    ['Cookie', 'Chocolate', 'Ice Cream', 'Cake'],
    ['Cookie', 'Chocolate', 'Donut'],
    ['Cookie', 'Chocolate', 'Cake'],
    ['Bread', 'Egg', 'Tomato'],
    ['Pizza', 'Burger'],
    ['Fries', 'Burger'],
]

te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)
```

Encoded output (subset):

| Cookie | Chocolate | Cake | Burger |
|--------|-----------|------|--------|
| 1      | 1         | 1    | 0      |
| 1      | 1         | 0    | 0      |
| 1      | 1         | 1    | 0      |
| 0      | 0         | 0    | 0      |
| 0      | 0         | 0    | 1      |
| 0      | 0         | 0    | 1      |

---

### 2. Frequent Itemset Generation

The Apriori algorithm was applied with a **minimum support threshold of 0.3**:

```python
from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
```

**Discovered Frequent Itemsets:**

| Itemset                    | Support |
|----------------------------|---------|
| Cookie                     | 0.50    |
| Chocolate                  | 0.50    |
| Cake                       | 0.33    |
| Burger                     | 0.33    |
| {Cookie, Chocolate}        | 0.50    |
| {Cake, Cookie}             | 0.33    |
| {Cake, Chocolate}          | 0.33    |
| {Cake, Cookie, Chocolate}  | 0.33    |

---

### 3. Association Rule Generation

Rules were generated using **confidence** as the metric with a **minimum confidence of 0.6**:

```python
from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
```

**Generated Association Rules:**

| Antecedent  | Consequent  | Confidence | Lift |
|-------------|-------------|------------|------|
| Cookie      | Chocolate   | 1.00       | 2.0  |
| Chocolate   | Cookie      | 1.00       | 2.0  |
| Cake        | Cookie      | 1.00       | 2.0  |
| Cookie      | Cake        | 0.67       | 2.0  |

---

## 📊 Results & Insights

### ✅ Strong Bakery Association

A strong relationship exists between **Cookie**, **Chocolate**, and **Cake**:

- Cookie and Chocolate appear together in **50% of all transactions**
- **Cookie → Chocolate** confidence = **100%** (customers who buy cookies always buy chocolate)
- **Lift = 2.0** confirms a strong positive association (well above the neutral value of 1)

### 🍔 Independent Fast-Food Cluster

A separate purchasing group was identified:

- **Burger**, **Fries**, and **Pizza** appear independently
- These items show **no association** with bakery items

---

## 💡 Business Recommendations

Based on the analysis, the following actions are suggested:

| Recommendation | Rationale |
|----------------|-----------|
| 🏪 Place Cookie & Chocolate on adjacent shelves | 100% co-purchase confidence |
| 🎁 Offer Cookie + Chocolate combo discounts | High support (50%) makes bundling profitable |
| 🎂 Bundle Cake with bakery promotions | Cake consistently co-occurs with bakery items |
| 🍟 Create a dedicated fast-food section | Burger/Fries cluster is entirely separate |

---

## 🧾 Conclusion

The Apriori analysis reveals **two distinct customer purchasing clusters**:

1. **Bakery cluster** – Cookie, Chocolate, and Cake are strongly associated with lift = 2.0
2. **Fast-food cluster** – Burger, Fries, and Pizza are purchased independently

These patterns can directly inform store layout, promotional strategies, and inventory planning.

---

## 🔮 Future Work

- [ ] Apply Apriori on a **larger, real-world dataset**
- [ ] Compare performance with the **FP-Growth Algorithm**
- [ ] **Visualize** association rules using network graphs
- [ ] Experiment with different support and confidence thresholds
- [ ] Deploy as an **interactive dashboard**

---
