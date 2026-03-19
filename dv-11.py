import matplotlib.pyplot as plt

# Realistic dataset (marks out of 100)
math_marks     = [78, 85, 92, 88, 76, 95, 89, 84, 91, 87]
science_marks  = [82, 79, 88, 91, 85, 87, 90, 84, 89]
english_marks  = [75, 80, 78, 82, 77, 79, 81, 83, 76, 80]

# Combine data
data = [math_marks, science_marks, english_marks]

# Create Box plot
plt.boxplot(data)

# Labels
plt.xticks([1, 2, 3], ['Math', 'Science', 'English'])
plt.title("Box plot of student marks")
plt.ylabel("Marks")          # <-- fixed typo

# Show plot
plt.show()
