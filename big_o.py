import time

# Function 1: The "Loop" Way (O(N) - Linear Time)
# This has to count 1, 2, 3... all the way to N. Slow!
def sum_loop(n):
    start = time.time()
    total = 0
    for i in range(1, n + 1):
        total += i
    end = time.time()
    print(f"Loop Result: {total}")
    print(f"Loop Time: {end - start:.10f} seconds")

# Function 2: The "Math" Way (O(1) - Constant Time)
# This uses one formula. Instant!
def sum_math(n):
    start = time.time()
    total = n * (n + 1) // 2
    end = time.time()
    print(f"Math Result: {total}")
    print(f"Math Time: {end - start:.10f} seconds")

# Test with a huge number (100 Million)
N = 100000000
print(f"Testing with N = {N}...")

sum_loop(N)
sum_math(N)
