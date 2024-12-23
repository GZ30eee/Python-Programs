# Height to Centimeters
feet = int(input("Enter height in feet: "))
inches = int(input("Enter height in inches: "))
total_inches = (feet * 12) + inches
cm = total_inches * 2.54
print(f"Height in centimeters: {cm}")
