# Triple Sum with Equality Rule
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b or b == c or a == c:
    print(0)
else:
    print(a + b + c)
