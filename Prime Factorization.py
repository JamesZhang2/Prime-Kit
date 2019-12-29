# Written by James Zhang on December 28, 2019
print("This program gives the prime factorization of a number.")
num = int(input("Enter a postive integer: "))
def PrimeCheck(a):
    isPrime = True
    for i in range (2, int(a**0.5) + 1):
        if a % i == 0:
            isPrime = False
    return isPrime

pfactor = str(num) + " = "
while num < 1:
    num = int(input("Enter a POSITIVE integer: "))
if num == 1:
    print("1 = 1")
else:
    if PrimeCheck(num) == True:
        print(str(num) + " is a prime.")
    else:
        while PrimeCheck(num) == False:
            for i in range (2, int(num**5) + 1):
                if num % i == 0:
                    num /= i
                    pfactor += str(i)
                    pfactor += " * "
                    break
        pfactor += str(int(num))
        print(pfactor)
