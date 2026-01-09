import pandas as pd

"""
Q1. Basic statical operations apply basic statical operations
    on a dataset. for example compute the mean,median,mode,range
    ,quartiles,and variance for one or more attributes a.create a
    dataframe for students' information such name,graduation percentage
    and age. display average age of student,average of graduation percentage.
    and,also describe all basic statistics of data. (Hint: use describe()).
"""

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Kiran"],
    "Age": [20, 21, 22, 20, 23],
    "Percentage": [75, 82, 68, 90, 85]
})

print("Average Age:", df["Age"].mean())
print("Average Percentage:", df["Percentage"].mean())
print("\nBasic Statistics:")
print(df.describe())
