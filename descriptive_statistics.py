import pandas as pd
from pathlib import Path

# Load dataset
file_path = Path(__file__).resolve().parent.parent / "dataset" / "cleaned_dataset.csv"
df = pd.read_csv(file_path)

# Select numerical columns
numeric_columns = ["Age", "Quantity", "Unit_Price", "Total_Sales"]

# 1. Calculate Mean
print("\n--- MEAN ---")
print(df[numeric_columns].mean())

# 2. Calculate Median
print("\n--- MEDIAN ---")
print(df[numeric_columns].median())

# 3. Calculate Mode
print("\n--- MODE ---")
for col in numeric_columns:
    print(col, ":", df[col].mode().tolist())

# 4. Calculate Standard Deviation
print("\n--- STANDARD DEVIATION ---")
print(df[numeric_columns].std())

# 5. Minimum and Maximum
print("\n--- MINIMUM VALUES ---")
print(df[numeric_columns].min())

print("\n--- MAXIMUM VALUES ---")
print(df[numeric_columns].max())

# 6. Complete Statistical Summary
print("\n--- COMPLETE STATISTICAL SUMMARY ---")
summary = df[numeric_columns].describe()
print(summary)

# 7. Save statistical summary
output_path = Path(__file__).resolve().parent.parent / "report" / "descriptive_statistics.csv"
summary.to_csv(output_path)

print("\nStatistical summary saved successfully!")
