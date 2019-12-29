# Created by James Zhang on December 28, 2019
print("This program prints all the prime numbers between two numbers.")
low = int(input("Enter a positive lower bound: "))
while low < 1:
    low = int(input("Enter a POSITIVE integer: "))
upp = int(input("Enter a positive upper bound: "))
while upp < low:
    upp = int(input("Enter an integer greater or equal to the lower bound: "))
primeList = []

count = 0
for i in range (low, upp+1):
    IsPrime = True
    if i == 1:
        IsPrime = False
    if i > 1:
        for j in range (2,int(i**0.5) + 1):
            if i % j == 0:
                IsPrime = False
    if IsPrime == True:
        primeList.append(i)
        count += 1

print("The prime numbers between " + str(low) + " and " + str(upp) + " are:" )
print(primeList)
print("There are " + str(count) + " prime numbers between " + str(low) + " and " + str(upp) + ".")
