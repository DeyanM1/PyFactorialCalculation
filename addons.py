import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
from mpmath import mp
import os


def countDigits(num: int) -> int:
    if num == 0:
        return 1
    # Use logarithm base 10 to count digits
    return math.floor(math.log10(num)) + 1

def displayCurrentNum(num: int, result: int) -> None:
    print(f"Multiplier: {num}  |  {result}")

def displayOnlyMultiplier(num: int) -> None:
    print(f"Multiplier: {num}")
  
def initFile(filename: str) -> None:
    with open(filename, 'w') as file: 
        pass
        
def writeToFile(filename: str, line: str) -> None:  
    with open(filename, 'r+') as file:
        lines = file.readlines()
    
    lines.append(line+"\n")
    
    with open(filename, 'w') as file:
        file.writelines(lines)
        
        
    """
#addons.writeToFile(fileName, "\n\n")
addons.writeToFile(fileName, f"Numbers: {numbers}")
addons.writeToFile(fileName, "----------------")
#addons.writeToFile(fileName, f"Calculation: {calculation}")
addons.writeToFile(fileName, f"Result: {result}")
addons.writeToFile(fileName, f"Digits: {digits}")
addons.writeToFile(fileName, f"Time elapsed: {t2 - t1}s")"""
        
def calcCalculation(numToFactorize: int) -> str:
    parts = []

    # Iterate from numToFactorize-1 down to 1
    for num in range(numToFactorize - 1, 0, -1):
        parts.append(f" * {num}")

    # Join all parts into a single string
    calculation = "".join(parts)
    
    return calculation
    #calculation = addons.calcCalculation(result)


def createChart(result: int, numToFactorize: int, show:bool=True) -> dict:
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in str(result):
        numbers[int(num)] += 1
    
    
    keys = list(numbers.keys())
    values = list(numbers.values())

    # Create the bar chart
    plt.bar(keys, values, color='skyblue')

    # Add labels and title
    plt.xlabel('Numbers')
    plt.ylabel('Frequency')
    plt.title('Bar Chart of Number Frequencies')
    
    plt.ylim(0, 8000)

    plt.savefig(f'charts/bar_chart{numToFactorize}.png')
    # Display the chart
    if show:
        plt.show()

    return numbers

def displayAsCurve(results: list, multiplier: list) -> None:   

    # x_data can be the indices of the list
    x_data = results  # x-values as indices (0, 1, 2, ...)

    # y_data are the values in the list
    y_data = multiplier

    # From here the plotting starts

    plt.plot(x_data, y_data, marker='o', label='Curve from list')  # Plot with markers for each point
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Curve Displayed by Elements in a List')
    plt.legend()
    plt.show()
