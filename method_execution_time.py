# Method Execution Time
import time
start_time = time.time()
# Example method: calculating the sum of first 1 million numbers
result = sum(range(1000000))
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
