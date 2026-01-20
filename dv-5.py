import pandas as pd

#Step-1: Read the Iris Dataset CSV file
df=pd.read_csv("SOCR-HeightWeight.csv")

print(f"\nTotal missing of NaN values in the dataset: {total_missing}")

#Step-2: Missing or NaN values in each column
missing_per_columxn