import pandas as pd

#Step-1: Read the Iris Dataset CSV file
df=pd.read_csv("iris.csv")

#Step-2: Display First few rows of the dataset
print("Iris Dataset:\n")
print(df.head())

#Step-3: Take random samples from the entire dataset:
print("\nRandom Sample from Dataset:\n")
print(df.sample(10))

#Step-4: Display maximum value of all numeric attribute:
print("\nMaximum value of numeric attributes:\n")
print(df.max(numeric_only=True))

#Step-5: Display total number of records
print("\nTotal number of records in dataset:")
print (len(df))

#Step-6: Count number of records for each distinct class (species)
print("\nNumber of records for each species:")
class_count=df['species'].value_counts()
print(class_count)

#Step-7: Display column_wise mean(numeric columns only)
print("\nColumn-wise Mean:")
mean_values=df.mean(numeric_only=True)