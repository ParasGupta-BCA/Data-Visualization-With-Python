import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Sneha', 'Ravi', 'Amit', None],
    'Age': [23, 25, np.nan, 23, 30],
    'Marks': [85, 90, 88, 85, None],
    'Date': ['2025-01-01', '2025-01-07', '2025-01-01', '2025-01-10', '2025-01-15']
}

df = pd.DataFrame(data)
print(df)
df.loc[row_label,column_label]

df.loc[2]