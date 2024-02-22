""" Subtract 2 numbers without - operator """


def subtract_without_operator(a, b):
    b_complement = ~b + 1
    return a + b_complement


result = subtract_without_operator(10, 5)
print(result)
