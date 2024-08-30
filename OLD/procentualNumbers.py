import time
import sys
import matplotlib.pyplot as plt
import seaborn as sns

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


def createChart(numbers):
    keys = list(numbers.keys())
    values = list(numbers.values())

    # Create the bar chart
    plt.bar(keys, values, color='skyblue')

    # Add labels and title
    plt.xlabel('Numbers')
    plt.ylabel('Frequency')
    plt.title('Bar Chart of Number Frequencies')

    plt.savefig(f'bar_chart{numToFactorize}.png')
    # Display the chart
    plt.show()

t1 = time.time()
result, calculation = calculate(numToFactorize)
t2 = time.time() 


n = result
digits = 0
while n > 0:
    n //= 10
    digits += 1
    




writeToFile("\n\n")

"""for elem in range(len(numbers)):
    print(f"[{elem}]: {numbers[elem]}")
    writeToFile(f"[{elem}]: {numbers[elem]}")"""
        

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