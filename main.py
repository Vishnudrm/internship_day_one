import pandas as pd

# Load CSV with correct encoding
print("Loading data...")
df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')

# Start report list
report = []
report.append("DATA CLEANING REPORT")
report.append("=" * 50)

# Initial info

print("\nFirst 5 rows:")
print(df.head())

print("\nInitial Data Info:")
print(df.info())

print("\nDescriptive Stats:")
print(df.describe())

report.append(f"\nInitial Shape: {df.shape}")
report.append("\nMissing Values (before cleaning):")
report.append(str(df.isnull().sum()))

print("\nMissing Values (before cleaning):")
print(df.isnull().sum())

# Fill numeric columns with mean
print("\nHandling missing values in numeric columns...")
for col in df.select_dtypes(include='number').columns:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)
        print(f"Filled missing values in numeric column '{col}' with mean.")
        report.append(f"Filled missing numeric values in '{col}' with mean.")

# Fill object columns with 'unknown'
print("\nHandling missing values in string columns...")
for col in df.select_dtypes(include='object').columns:
    if df[col].isnull().sum() > 0:
        df[col].fillna('unknown', inplace=True)
        print(f"Filled missing values in string column '{col}' with 'unknown'.")
        report.append(f"Filled missing string values in '{col}' with 'unknown'.")

# Convert ORDERDATE to datetime
if 'ORDERDATE' in df.columns:
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
    print("Converted 'ORDERDATE' to datetime format.")
    report.append("Converted 'ORDERDATE' to datetime format.")

# Clean string columns (trim & lowercase)
print("\nCleaning up string columns (strip & lowercase)...")
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.lower()

# Drop duplicates
before_dedup = df.shape[0]
df.drop_duplicates(inplace=True)
after_dedup = df.shape[0]
removed = before_dedup - after_dedup
print(f"\nRemoved {removed} duplicate rows.")
report.append(f"Removed {removed} duplicate rows.")

# Final shape & null check
print("\nFinal cleaned data shape:", df.shape)
print("\nMissing values (after cleaning):")
print(df.isnull().sum())

report.append(f"\nFinal Shape: {df.shape}")
report.append("\nMissing Values (after cleaning):")
report.append(str(df.isnull().sum()))

# Save report to TXT
print("\nSaving report to 'cleaning_report.txt'...")
with open("cleaning_report.txt", "w", encoding='utf-8') as f:
    f.write("\n".join(report))

# Save cleaned data to Excel
print("Saving cleaned data to 'cleaned_sales_data.xlsx'...")
df.to_excel("cleaned_sales_data.xlsx", index=False)

print("\nCleaning complete. Files saved successfully.")
