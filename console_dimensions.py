# Console Dimensions
import os
rows, columns = os.popen('stty size', 'r').read().split()
print(f"Rows: {rows}, Columns: {columns}")
