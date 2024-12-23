# Seconds to DHMS Converter
seconds = int(input("Enter seconds: "))
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
