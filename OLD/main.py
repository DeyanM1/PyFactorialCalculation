import time
import sys

sys.set_int_max_str_digits(50000)



numToFactorize = int(input("Enter number to factorize -> "))




result = 1
calculation = str(numToFactorize)

for num in range(numToFactorize-1, 0, -1):
    if num != 0:
        calculation += f" * {num}"
        
        
t1 = time.time()
for num in range(numToFactorize, 0, -1):
    if num != 0:
        result = result * num
        print(f"Multiplier: {num}  |  {result}")
t2 = time.time()     


n = result
digits = 0
while n > 0:
    n //= 10
    digits += 1

        

print("------------------")
print(f"Calculation: {calculation}")
print(f"Result: {result}")
print(f"Digits: {digits}")
print(f"Time elapsed: {t2 - t1}s")