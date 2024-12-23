# Pressure Unit Converter
kpa = float(input("Enter pressure in kilopascals: "))
psi = kpa / 6.89476
mmHg = kpa * 7.50062
atm = kpa / 101.325
print(f"Pressure in psi: {psi:.2f}, mmHg: {mmHg:.2f}, atm: {atm:.2f}")
