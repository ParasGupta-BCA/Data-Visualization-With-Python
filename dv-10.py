import matplotlib.pyplot as plt

# Subject names
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English']

# Marks obtained in each subject (0‑100 scale)
marks = [85, 78, 92, 88, 76]

# Create a figure with two subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# -------------------- Pie Chart --------------------
ax1.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.tab20.colors
)
ax1.set_title('Marks Distribution – Pie Chart')

# -------------------- Bar Chart --------------------
bars = ax2.bar(
    subjects,
    marks,
    color='skyblue',
    edgecolor='black'
)
ax2.set_xlabel('Subject')
ax2.set_ylabel('Marks')
ax2.set_title('Marks Distribution – Bar Chart')
ax2.set_ylim(0, 100)

# Optional: add the numeric value on top of each bar
for bar in bars:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f'{height}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Adjust layout so that titles and labels don't overlap
fig.tight_layout()

plt.show()
