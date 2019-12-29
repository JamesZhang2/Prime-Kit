print("This program tests whether a number is prime or not.")
num = int(input("Enter a postive integer: "))
IsPrime = True
while num < 1:
    num = int(input("Enter a POSITIVE integer: "))
if num == 1:
    IsPrime = False
if num > 1:
    for i in range (2,int(num**0.5) + 1):
        if num % i == 0:
            IsPrime = False

if IsPrime == True:
    print(num, "is a prime.")
else:
    print(num, "is not a prime.")
