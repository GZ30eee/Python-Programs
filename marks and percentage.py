marks = {}
subjects = ["Maths", "Science", "English", "Social Studies", "Computer Science"]

# Take marks from the user
for subject in subjects:
    marks[subject] = float(input(f"Enter the marks for {subject}: "))

total_marks = sum(marks.values())
percentage = (total_marks / (len(subjects) * 100)) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
