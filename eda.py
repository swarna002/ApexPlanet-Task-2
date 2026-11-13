import pandas as pd
from pathlib import Path

# Load the dataset
file_path = Path(__file__).resolve().parent.parent / "dataset" / "cleaned_dataset.csv"

df = pd.read_csv(file_path)

# 1. Display first five rows
print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# 2. Dataset dimensions
print("\n--- DATASET SHAPE ---")
print("Rows and Columns:", df.shape)

# 3. Column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 4. Dataset information
print("\n--- DATASET INFORMATION ---")
df.info()

# 5. Statistical summary
print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe(include="all"))

# 6. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 7. Duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Total duplicates:", df.duplicated().sum())

# 8. Data types
print("\n--- DATA TYPES ---")
print(df.dtypes)
