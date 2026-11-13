
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("../dataset/cleaned_dataset.csv")

# Create report folder
os.makedirs("../report/plots", exist_ok=True)

# Set visualization style
sns.set_theme(style="whitegrid")

# 1. Sales by Category
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Category", y="Total_Sales", estimator="sum", errorbar=None)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../report/plots/sales_by_category.png")
plt.close()

print("Sales by Category chart saved successfully!")


# 2. Sales Distribution by Gender
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Gender", y="Total_Sales", estimator="sum", errorbar=None)
plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("../report/plots/sales_by_gender.png")
plt.close()

print("Sales by Gender chart saved successfully!")


# 3. Top 10 Cities by Sales
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
city_sales.plot(kind="bar")
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../report/plots/top_10_cities.png")
plt.close()

print("Top 10 Cities chart saved successfully!")


# 4. Quantity Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Quantity", bins=10, kde=True)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../report/plots/quantity_distribution.png")
plt.close()

print("Quantity Distribution chart saved successfully!")


# 5. Correlation Heatmap

# Select numerical columns
numeric_df = df[["Age", "Quantity", "Unit_Price", "Total_Sales"]]

# Calculate correlation
correlation = numeric_df.corr()

# Create heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("../report/plots/correlation_heatmap.png")
plt.close()

print("Correlation Heatmap saved successfully!")
