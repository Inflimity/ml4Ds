# 🏟️ Level 1: The Analyst (Foundations)

Welcome, Junior Analyst. Your first priority is understanding the data before we ever think about building a model.

## 🎯 Primary Objective
Generate a **Correlation Heatmap** to identify what drives sales, and prepare the final **Cleaned Dataset** for the machine learning team.

---

## 🛠️ Step-by-Step Instructions

1.  **🔍 Load your Data:**
    Ensure you can load `data/sales_dataset.csv` using pandas.
2.  **📈 Visual Correlation:**
    Create a heatmap using `seaborn`. (You've already started this in `eda.py`!).
3.  **🧹 The Cleanup:**
    - Identify columns that are purely numeric.
    - Drop any `CustomerID` or `ID` columns that don't help prediction.
    - Save this ready-to-use data as `cleaned_data.csv`.

---

## ✅ Level 1 Success Criteria
- [ ] A file named `heatmap.png` exists in the root directory.
- [ ] A file named `cleaned_data.csv` exists in the root directory.
- [ ] **The Benchmark:** Your reported correlations must match the **Scientific Lead's** benchmarks (+/- 5%).

---

### 🛡️ Senior Lead's Tip:
*"An Analyst reports what is. A Scientist prepares what will be. Look for the columns that have the darkest colors in your heatmap — those are your future Features."*

---

> [!CAUTION]
> **DO NOT** attempt to run any `LinearRegression` yet. You are an Analyst. Your goal is the data, not the model. Use Level 2 for the model.
