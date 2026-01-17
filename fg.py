import csv
import pandas as pd
with open(r"C:\Users\student\Downloads\archive (2)\iris.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        print(row)
