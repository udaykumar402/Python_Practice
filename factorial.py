""" To find factorial of given number using inbuilt methods"""
import math


# Method_1:
def factorial_inbuilt(num):
    print(f"Factorial of {num} : ", math.factorial(num))


fact_num = 5
factorial_inbuilt(fact_num)


# Method_2

def factorial_without_inbuilt(num):
    result = 1
    for number in range(1, num+1):
        result *= number
    print(f"Factorial of {num} : ", result)


fact_number = 5
factorial_without_inbuilt(fact_number)
