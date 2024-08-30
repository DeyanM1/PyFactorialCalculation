import time
import sys
import addons


sys.set_int_max_str_digits(1000000)

numToFactorize = 0
results = []
multiplier = []

while numToFactorize <= 10:
    result = 1

    fileName = f"values/Factorize{numToFactorize}.txt"
    addons.initFile(fileName)

    t1 = time.time()
    for num in range(numToFactorize, 0, -1):
        if num != 0:
            result = result * num
        addons.displayOnlyMultiplier(num)
    t2 = time.time()    

    #numbers = addons.createChart(result, numToFactorize, False)
    digits = addons.countDigits(result)

    


    print("------------------")
    print(f"Result: {result}")
    #print(f"Calculation: {calculation}")
    print(f"Digits: {digits}")
    print(f"Time elapsed: {t2 - t1}s")

    results.append(result)
    multiplier.append(numToFactorize)
    numToFactorize += 1
    
print(results)
addons.displayAsCurve(results, multiplier)