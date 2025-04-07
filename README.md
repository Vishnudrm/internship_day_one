# 🧹 Sales Data Cleaning Script

This project is a Python-based script designed to clean and preprocess a sample sales dataset. The script helps data analysts and developers streamline the cleaning process before performing exploratory data analysis (EDA) or building data models.

It reads a raw CSV file (`sales_data_sample.csv`), handles missing values, converts date fields, formats strings, removes duplicates, and finally outputs a cleaned Excel file and a detailed cleaning report.

---

## 📌 Objective

In real-world scenarios, raw datasets often contain:
- Missing or inconsistent values
- Incorrect data types (e.g., strings instead of dates)
- Duplicate entries
- Unformatted text

This script automates the cleaning process to ensure your data is analysis-ready.

---

## 🗂️ Files Included

| File Name                  | Description                                      |
|---------------------------|--------------------------------------------------|
| `sales_data_sample.csv`   | Raw sales dataset (input)                        |
| `cleaned_sales_data.xlsx` | Cleaned version of the dataset (output)          |
| `cleaning_report.txt`     | Summary of all data cleaning operations (output) |
| `clean_sales_data.py`     | Python script to execute the cleaning process    |

---

## 🧰 Features

Here’s what the script does, step by step:

- ✅ **Loads data** with the correct encoding (`ISO-8859-1`)
- 👀 Displays initial data snapshot: head, info, and basic statistics
- 🔍 Detects and reports missing values
- 🔢 **Handles missing values:**
  - Fills missing numeric columns with the **mean**
  - Fills missing categorical columns with `"unknown"`
- 🗓️ Converts `ORDERDATE` column to proper **datetime format**
- 🧼 **Cleans string fields**:
  - Trims whitespaces
  - Converts text to lowercase
- 🧹 **Removes duplicate rows**
- 📄 **Saves report** with cleaning steps in `cleaning_report.txt`
- 📁 **Exports cleaned data** as `cleaned_sales_data.xlsx`

---

## 🐍 Requirements

Ensure you have the following installed:

- Python 3.x
- pandas

Install required packages using:

```bash
pip install pandas
