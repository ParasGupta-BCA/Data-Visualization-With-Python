import pandas as pd

# Step-1. Load the dataset
df = pd.read_csv('retail.csv')

# Step-2. Handle Missing Data
df['Sales_Amount'] = df['Sales_Amount'].fillna(df['Sales_Amount'].mean())
df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].mean())

# Step-3. Understand Central Tendency of Sales
sales_mean = df['Sales_Amount'].mean()
sales_median = df['Sales_Amount'].median()
sales_mode = df['Sales_Amount'].mode()[0]

print("--- Central Tendency of Sales ---")
print(f"Mean:   {sales_mean:.2f}")
print(f"Median: {sales_median:.2f}")
print(f"Mode:   {sales_mode:.2f}\n")

# Step-4. Analyze Branch Performance
branch_performance = df.groupby('Branch_ID')[['Sales_Amount', 'Customer_Rating']].mean()

# Step-5. Identify High-Performing Branches
high_performing_branches = branch_performance.sort_values(by='Sales_Amount', ascending=False)

print("--- Branch Performance Analysis ---")
print(high_performing_branches)

# Step-6. Summary of High-Performing Branches
top_branch = high_performing_branches.index[0]
print(f"\nThe highest performing branch overall is: {top_branch}")