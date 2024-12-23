# Line Midpoint Calculator
x1, y1 = map(float, input("Enter x1 and y1: ").split())
x2, y2 = map(float, input("Enter x2 and y2: ").split())
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"The midpoint of the line is {midpoint}")
