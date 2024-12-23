# Directory Listing by Creation Date
import os
directory = input("Enter directory path: ")
files = os.listdir(directory)
files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))
print("Directory listing sorted by creation date:")
for file in files:
    print(file)
