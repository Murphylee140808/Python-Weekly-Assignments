# Data Analysis and Visualization Assignment

## 📌 Objective

The objective of this assignment is to:

- Load and analyze a dataset using the **pandas** library in Python.
- Perform basic data exploration and analysis.
- Create simple plots and charts using **matplotlib** (and optionally seaborn) for visualization.
- Summarize findings and observations.

---

## 📂 Dataset

For this assignment, I used the **Heart Disease dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease).

Steps taken:

1. Imported the dataset programmatically using the `ucimlrepo` Python library.
2. Saved the dataset into CSV format (`heart_disease.csv`) to comply with the assignment requirement of loading a CSV file.
3. Reloaded the CSV using pandas for further analysis and visualization.

---

## 📝 Tasks Completed

### Task 1: Load and Explore the Dataset

- Loaded `heart_disease.csv` using **pandas**.
- Displayed the first few rows of the dataset with `.head()`.
- Inspected the dataset structure with `.info()` and checked for missing values with `.isnull().sum()`.
- Cleaned the dataset by dropping or filling missing values.

### Task 2: Basic Data Analysis

- Computed summary statistics of numerical columns with `.describe()`.
- Grouped the dataset by a categorical variable (`sex`) and calculated the average of a numerical variable (`age`).
- Highlighted patterns such as differences in average age between male and female patients.

### Task 3: Data Visualization

Created the following plots using **matplotlib** and **seaborn**:

1. **Line chart** – Age trend across the first 50 patients.
2. **Bar chart** – Average age by sex.
3. **Histogram** – Distribution of cholesterol levels.
4. **Scatter plot** – Relationship between age and maximum heart rate (`thalach`).

All plots were customized with appropriate titles, axis labels, and legends.

---

## 📊 Tools and Libraries Used

- **Python 3**
- **pandas** – data loading, cleaning, and analysis
- **matplotlib** – data visualization
- **seaborn** – additional styling for charts
- **ucimlrepo** – fetching dataset from UCI repository

---

## ✅ Findings and Observations

- The dataset provides insights into patient characteristics related to heart disease.
- Average age varies by sex, with men being slightly older on average in the dataset.
- Cholesterol levels show a wide distribution, suggesting variation in patient health.
- There is a visible relationship between age and maximum heart rate (`thalach`), which typically decreases with age.

---

## 🚀 How to Run the Code

1. Clone or download this project folder.
2. Install dependencies if not already available:

   ```bash
   pip install pandas matplotlib seaborn ucimlrepo
   ```
3. Open the Jupyter Notebook (`HeartDisease_analysis.ipynb`) 
4. Ensure `heart_disease.csv` is in the same folder as the notebook/script.

---

## 📁 Submission Contents

* `HeartDisease_analysis.ipynb` – Jupyter Notebook with code, outputs, and explanations
* `heart_disease.csv` – Dataset used for analysis
* `README.md` – This documentation file
