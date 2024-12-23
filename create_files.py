import os

# Programs and their content
programs = [
    ("print_to_stderr.py", 
     """# Print to STDERR
import sys
sys.stderr.write("This is an error message\\n")
"""),
    ("access_environment_variables.py", 
     """# Access Environment Variables
import os
print(os.environ)
"""),
    ("get_current_username.py", 
     """# Get Current Username
import getpass
print(getpass.getuser())
"""),
    ("find_local_ips.py", 
     """# Find Local IPs
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Local IP address: {local_ip}")
"""),
    ("console_dimensions.py", 
     """# Console Dimensions
import os
rows, columns = os.popen('stty size', 'r').read().split()
print(f"Rows: {rows}, Columns: {columns}")
"""),
    ("method_execution_time.py", 
     """# Method Execution Time
import time
start_time = time.time()
# Example method: calculating the sum of first 1 million numbers
result = sum(range(1000000))
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
"""),
    ("sum_first_n_positives.py", 
     """# Sum of First n Positive Integers
n = int(input("Enter a positive integer: "))
print(f"The sum of the first {n} positive integers is {n * (n + 1) // 2}")
"""),
    ("height_to_cm.py", 
     """# Height to Centimeters
feet = int(input("Enter height in feet: "))
inches = int(input("Enter height in inches: "))
total_inches = (feet * 12) + inches
cm = total_inches * 2.54
print(f"Height in centimeters: {cm}")
"""),
    ("triangle_hypotenuse.py", 
     """# Triangle Hypotenuse Calculator
import math
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
hypotenuse = math.sqrt(a**2 + b**2)
print(f"The hypotenuse of the triangle is {hypotenuse}")
"""),
    ("feet_to_units.py", 
     """# Feet to Other Units
feet = float(input("Enter distance in feet: "))
inches = feet * 12
yards = feet / 3
miles = feet / 5280
print(f"Inches: {inches}, Yards: {yards}, Miles: {miles}")
"""),
    ("time_to_seconds.py", 
     """# Time to Seconds Converter
days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
print(f"Total seconds: {total_seconds}")
"""),
    ("absolute_file_path.py", 
     """# Absolute File Path Finder
import os
file_name = input("Enter file name: ")
print(f"Absolute path: {os.path.abspath(file_name)}")
"""),
    ("file_timestamps.py", 
     """# File Timestamps
import os
import time
file_name = input("Enter file name: ")
print(f"Creation time: {time.ctime(os.path.getctime(file_name))}")
print(f"Modification time: {time.ctime(os.path.getmtime(file_name))}")
"""),
    ("seconds_to_dhms.py", 
     """# Seconds to DHMS Converter
seconds = int(input("Enter seconds: "))
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
"""),
    ("bmi_calculator.py", 
     """# BMI Calculator
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
"""),
    ("pressure_converter.py", 
     """# Pressure Unit Converter
kpa = float(input("Enter pressure in kilopascals: "))
psi = kpa / 6.89476
mmHg = kpa * 7.50062
atm = kpa / 101.325
print(f"Pressure in psi: {psi:.2f}, mmHg: {mmHg:.2f}, atm: {atm:.2f}")
"""),
    ("sum_of_digits.py", 
     """# Sum of Digits
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num if digit.isdigit())
print(f"The sum of digits is {digit_sum}")
"""),
    ("sort_three_numbers.py", 
     """# Sort Three Numbers
nums = list(map(int, input("Enter three integers: ").split()))
nums.sort()
print(f"Sorted numbers: {nums}")
"""),
    ("sort_files_by_date.py", 
     """# Sort Files by Date
import os
directory = input("Enter directory path: ")
files = os.listdir(directory)
files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))
print("Files sorted by creation date:")
for file in files:
    print(file)
"""),
    ("directory_listing_by_date.py", 
     """# Directory Listing by Creation Date
import os
directory = input("Enter directory path: ")
files = os.listdir(directory)
files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))
print("Directory listing sorted by creation date:")
for file in files:
    print(file)
"""),
    ("math_module_details.py", 
     """# Math Module Details
import math
print(dir(math))
"""),
    ("line_midpoint.py", 
     """# Line Midpoint Calculator
x1, y1 = map(float, input("Enter x1 and y1: ").split())
x2, y2 = map(float, input("Enter x2 and y2: ").split())
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"The midpoint of the line is {midpoint}")
"""),
    ("hash_word.py", 
     """# Word Hasher
import hashlib
word = input("Enter a word: ")
hashed_word = hashlib.sha256(word.encode()).hexdigest()
print(f"The SHA-256 hash of the word is {hashed_word}")
""")
]

# Create each file
for filename, content in programs:
    with open(filename, "w") as file:
        file.write(content)

print("Files created successfully!")