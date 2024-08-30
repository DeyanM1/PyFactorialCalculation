import time
import sys

sys.set_int_max_str_digits(500000)

numToFactorize = 30000
result = 1

t1 = time.time()
for num in range(numToFactorize, 0, -1):
    if num != 0:
        result = result * num
t2 = time.time()    

n = result
digits = 0
while n > 0:
    n //= 10
    digits += 1  

print(f"Result: {result}")
print(f"Digits: {digits}")
print(f"Elapsed: {t2 - t1}s")