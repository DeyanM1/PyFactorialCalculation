import time
import sys

sys.set_int_max_str_digits(50000)

numToFactorize = int(input("Enter number to factorize -> "))

fileName = "factorial.txt"
with open(fileName, 'w') as f: pass



def writeToFile(line):
    with open(fileName, 'r+') as file:
        lines = file.readlines()
    
    lines.append(line+"\n")
    
    with open(fileName, 'w') as file:
        file.writelines(lines)
        
def calculate(numToFactorize: int):

    result = 1
    calculation = str(numToFactorize)

    for num in range(numToFactorize-1, 0, -1):
        if num != 0:
            calculation += f" * {num}"
            
            

    for num in range(numToFactorize, 0, -1):
        if num != 0:
            result = result * num
            
            text = f"Multiplier: {num}  |  {result}"
            
            writeToFile(text)
            print(text)
            
    return result, calculation



t1 = time.time()
result, calculation = calculate(numToFactorize)
t2 = time.time() 


n = result
digits = 0
while n > 0:
    n //= 10
    digits += 1

        
writeToFile("\n\n")
writeToFile("----------------")
writeToFile(f"Calculation: {calculation}")
writeToFile(f"Result: {result}")
writeToFile(f"Digits: {digits}")
writeToFile(f"Time elapsed: {t2 - t1}s")

print("------------------")
print(f"Calculation: {calculation}")
print(f"Result: {result}")
print(f"Digits: {digits}")
print(f"Time elapsed: {t2 - t1}s")