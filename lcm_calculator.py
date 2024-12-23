# LCM Calculator
from math import gcd
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = abs(a * b) // gcd(a, b)
print(f"The LCM of {a} and {b} is {lcm}")
