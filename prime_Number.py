""" To check whether the given number is prime or not """


def primeNumber(num):
    flag = False
    for n in range(2, num):
        if num % n == 0:
            flag = True
            break
    if flag:
        print(num, " is not a prime number")
    else:
        print(num, " is a prime number")


number = 11
primeNumber(number)
