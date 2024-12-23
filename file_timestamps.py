# File Timestamps
import os
import time
file_name = input("Enter file name: ")
print(f"Creation time: {time.ctime(os.path.getctime(file_name))}")
print(f"Modification time: {time.ctime(os.path.getmtime(file_name))}")
