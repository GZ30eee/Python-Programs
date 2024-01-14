num_subjects = int(input("Enter the number of subjects: "))

marks = {}

for i in range(num_subjects):
    subject = input(f"Enter the name of subject {i+1}: ")
    marks[subject] = float(input(f"Enter the marks for {subject}: "))

total_marks = sum(marks.values())
percentage = (total_marks / (num_subjects * 100)) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
3
