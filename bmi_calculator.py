# BMI Calculator
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
