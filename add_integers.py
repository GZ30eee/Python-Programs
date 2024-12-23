# Add Integers Validator
a = input("Enter first value: ")
b = input("Enter second value: ")
if a.isdigit() and b.isdigit():
    print(int(a) + int(b))
else:
    print("Both inputs must be integers.")
