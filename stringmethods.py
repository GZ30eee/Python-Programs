# String for demonstration
s = "Hello, World!"

# capitalize()
print(s.capitalize())

# casefold()
print(s.casefold())

# center()
print(s.center(20))

# count()
print(s.count('o'))

# encode()
print(s.encode())

# endswith()
print(s.endswith('!'))

# expandtabs()
print("H\te\tl\tl\to".expandtabs(2))

# find()
print(s.find('o'))

# format()
print("Hello, {}!".format("Python"))

# format_map()
print("{x} {y}".format_map({'x': 'Hello', 'y': 'Python'}))

# index()
print(s.index('o'))

# isalnum()
print(s.isalnum())

# isalpha()
print(s.isalpha())

# isascii()
print(s.isascii())

# isdecimal()
print(s.isdecimal())

# isdigit()
print(s.isdigit())

# isidentifier()
print(s.isidentifier())

# islower()
print(s.islower())

# isnumeric()
print(s.isnumeric())

# isprintable()
print(s.isprintable())

# isspace()
print(s.isspace())

# istitle()
print(s.istitle())

# isupper()
print(s.isupper())

# join()
print('-'.join(['Hello', 'Python']))

# ljust()
print(s.ljust(20))

# lower()
print(s.lower())

# lstrip()
print("   Hello, Python   ".lstrip())

# maketrans() and translate()
trans = s.maketrans('H', 'J')
print(s.translate(trans))

# partition()
print(s.partition(','))

# replace()
print(s.replace('Hello', 'Hi'))

# rfind()
print(s.rfind('o'))

# rindex()
print(s.rindex('o'))

# rjust()
print(s.rjust(20))

# rpartition()
print(s.rpartition(','))

# rsplit()
print(s.rsplit(','))

# rstrip()
print("   Hello, Python   ".rstrip())

# split()
print(s.split(','))

# splitlines()
print("Hello\nPython".splitlines())

# startswith()
print(s.startswith('H'))

# strip()
print("   Hello, Python   ".strip())

# swapcase()
print(s.swapcase())

# title()
print(s.title())

# upper()
print(s.upper())

# zfill()
print(s.zfill(20))