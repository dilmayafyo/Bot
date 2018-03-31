numbers = "10 20 34 2 55"

listOfNumbers = numbers.split(" ")

sumNums = 0

for num in listOfNumbers:
    sumNums += int(num)

print(sumNums)
