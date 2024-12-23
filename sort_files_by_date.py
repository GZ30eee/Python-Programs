# Sort Files by Date
import os
directory = input("Enter directory path: ")
files = os.listdir(directory)
files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))
print("Files sorted by creation date:")
for file in files:
    print(file)
