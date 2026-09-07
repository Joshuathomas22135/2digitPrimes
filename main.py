listOfPrimes = []

for i in range(100):
    listOfPrimes.append(True)


listOfPrimes[0] = False
listOfPrimes[1] = False

for j in range(2, len(listOfPrimes)):
    for k in range(2, j):
        if j % k == 0:
            listOfPrimes[j] = False

for i in range(10, 100):
    if listOfPrimes[i] == True:
        print(i)