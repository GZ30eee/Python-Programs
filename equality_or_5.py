# Equality or 5 Rule Checker
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b or abs(a - b) == 5 or (a + b) == 5:
    print(True)
else:
    print(False)
