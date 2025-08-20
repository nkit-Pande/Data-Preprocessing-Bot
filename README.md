# 🤖 Data Preprocessing Bot

A **lightweight yet powerful Python utility** that automates common **data preprocessing tasks** — the backbone of every data analysis and machine learning workflow.

This project was built to **standardize preprocessing steps** and ensure datasets are **clean, consistent, and ML-ready** with minimal effort.

---

## ✨ Key Features

✅ **Smart Missing Value Handling**

* Numeric columns → filled with **mean**
* Categorical columns → filled with **mode**

✅ **Seamless Categorical Encoding**

* **Label Encoding** → binary categorical features
* **One-Hot Encoding** → multi-class categorical features

✅ **Flexible Feature Scaling**

* **Standardization (Z-score):** centers around mean 0 with variance 1
* **Normalization (Min-Max):** rescales features to `[0, 1]`

✅ **Train-Test Split Made Easy**

* Automatic dataset partitioning for **fair model evaluation**

✅ **Transparent Reporting**

* Generates a summary of:

  * Missing value handling
  * Encoding strategy
  * Scaling method
  * Train/Test split

---

## 🏗️ Project Structure

```bash
Data-Preprocessing-Bot/
│── preprocessor.py     # Core preprocessing engine  
│── cli.py              # CLI tool for running preprocessing  
│── logger.py           # Logging utility for clean outputs  
│── sample.csv          # Example dataset  
│── README.md           # Project documentation  
│── requirements.txt    # Dependencies  
```

---

## ⚙️ Installation

Clone the repo:

```bash
git clone https://github.com/your-username/Data-Preprocessing-Bot.git
cd Data-Preprocessing-Bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run preprocessing in **one line**:

```bash
python cli.py --file sample.csv --target Salary --scaling standard --test-size 0.2
```

🔹 **Arguments**

* `--file` → Path to dataset (.csv / .xlsx)
* `--target` → Target column for supervised learning
* `--scaling` → `standard` | `minmax`
* `--test-size` → Test set proportion (default: 0.2)

---

## 📊 Why This Project?

In real-world ML projects, **80% of the time** is spent on data preprocessing, not modeling.
This project:

* Automates repetitive preprocessing steps
* Ensures **consistency** across datasets
* Provides a **ready-to-use foundation** for ML pipelines

---

## 📖 Summary

This bot encapsulates **essential preprocessing steps**:

* 🧹 Handling Missing Data → ensures data completeness
* 🔤 Encoding Categorical Features → converts text into numbers
* 📏 Feature Scaling → aligns feature ranges for better performance
* ✂️ Data Splitting → avoids biased evaluations

By combining these into a **single automated pipeline**, it offers a **reusable and extensible framework** for ML projects.

---

⚡ *Clean data, faster experiments, better models.* ⚡

---
