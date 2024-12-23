# Future Value Calculator
amt = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))
future_value = amt * ((1 + (rate / 100)) ** years)
print(f"Future value: {future_value:.2f}")
