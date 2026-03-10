# Student Marks Analysis
> Python Data Analysis & Visualization Project

---

## Overview

This project generates a **synthetic student marks dataset** using NumPy's statistical distributions, computes grade classifications, saves the results as a CSV file, and produces a comprehensive **5-panel visualization** using Matplotlib.

It demonstrates an end-to-end data science workflow: data generation → processing → analysis → visualization.

---

## Requirements

| Package | Purpose |
|---|---|
| `numpy` | Numerical computing & random distributions |
| `matplotlib` | Data visualization & charting |
| `pandas` | DataFrame creation & CSV export |

Install all dependencies:

```bash
pip install numpy matplotlib pandas
```

---

## How to Run

```bash
python student_marks_analysis.py
```

This will:
- Generate a dataset of **50 students**
- Save it as `student_marks_dataset.csv` in the current directory
- Display a Matplotlib window with **5 charts**

---

## Code Walkthrough

### Step 1 — Dataset Generation

50 students are generated with marks in 3 subjects, each using a different statistical distribution:

| Subject | Distribution | Parameters | Rationale |
|---|---|---|---|
| Mathematics | Normal | mean=70, std=10 | Scores cluster around a central average |
| Physics | Uniform | low=50, high=90 | Equal likelihood across the full range |
| Programming | Gamma | shape=5, scale=10 | Right-skewed — harder subject, lower scores more common |

All marks are clipped to the valid range **[0, 100]** using `np.clip()`.

---

### Step 2 — Grade Classification

The average mark is the arithmetic mean of all three subjects. Grades are assigned as:

| Grade | Condition | Meaning |
|---|---|---|
| A | Average ≥ 80 | Distinction |
| B | Average ≥ 65 | Merit |
| C | Average ≥ 50 | Pass |
| D | Average < 50 | Fail |

---

### Step 3 — DataFrame & CSV Export

A Pandas DataFrame is assembled with columns:

```
Student_ID | Mathematics | Physics | Programming | Average | Grade
```

Marks are rounded to 2 decimal places and exported to `student_marks_dataset.csv`.

**Sample output (first 5 rows):**

```
   Student_ID  Mathematics  Physics  Programming  Average Grade
0           1        74.97    55.64        36.13    55.58     C
1           2        68.62    82.09        58.66    69.79     B
2           3        76.48    52.98        33.08    54.18     C
3           4        85.23    89.48        39.94    71.55     B
4           5        67.66    80.89        53.36    67.30     B
```

---

## Visualizations

A **2×3 subplot grid** (16×10 inches) is generated with 5 charts:

### Chart 1 — Bar Chart: Average Marks Across Subjects
Compares the mean score for Mathematics, Physics, and Programming side by side. Identifies which subject students performed best/worst in overall.

### Chart 2 — Histogram: Distribution of Programming Marks
Shows the frequency distribution of Programming marks across 10 bins. Because marks follow a Gamma distribution, the histogram displays a **right skew** — most students score lower with fewer high achievers.

### Chart 3 — Pie Chart: Grade Distribution
Displays the proportion of students in each grade category (A, B, C, D) as a percentage. Gives a quick snapshot of overall class performance.

### Chart 4 — Scatter Plot: Mathematics vs Physics Correlation
Plots each student as a point with Mathematics on the x-axis and Physics on the y-axis. Since the two subjects use independent distributions, **little to no correlation** is expected.

### Chart 5 — Box Plot: Spread Across Subjects
Shows the median, interquartile range (IQR), and outliers for all three subjects. Reveals variability differences:
- **Physics (Uniform)** → wide, even spread
- **Mathematics (Normal)** → classic symmetric box
- **Programming (Gamma)** → skewed with a long upper tail

---

## Output Files

| File | Description |
|---|---|
| `student_marks_dataset.csv` | Generated dataset — 50 rows, 6 columns |
| Matplotlib window | 5-panel visualization displayed on screen |

---

## Notes & Known Warnings

- `np.random.seed(42)` is set for **reproducibility** — the same dataset is generated on every run.
- The `grades` list is computed **twice** in the code (before and after the DataFrame). Both are identical; the second is redundant but harmless.
- On **Matplotlib 3.9+**, the following warning may appear:

  ```
  MatplotlibDeprecationWarning: The 'labels' parameter of boxplot() has been renamed 'tick_labels'
  ```

  To fix it, change this line in the boxplot call:
  ```python
  # Before
  plt.boxplot([...], labels=subject_names)

  # After
  plt.boxplot([...], tick_labels=subject_names)
  ```

---

*Student Marks Analysis — Python Data Visualization Project*
