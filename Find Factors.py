print("This program finds all the factors of a given number.")
num = int(input("Enter a postive integer: "))
while num < 1:
    num = int(input("Enter a POSITIVE integer: "))
if num == 1:
    print("The factor of 1 is 1.")
    print("There is 1 factor in total.")
else:
    factors = ""
    count = 0
    for i in range (1, num):
        if num % i == 0:
            factors = factors + str(i) + ","
            count += 1
    factors = factors + str(num) + "."  # All integers are factors of themselves
    count += 1
    print("The factors of " + str(num) + " are " + factors)
    print("There are " + str(count) + " factors in total.")
