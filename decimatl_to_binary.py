""" To find decimal to binary woth and without inbuilt methods """

# Method_1
decimal_value = 10
binary_value = bin(decimal_value)


# Method_2
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary


decimal_number = 123
print("Decimal:", decimal_number)
print("Binary:", decimal_to_binary(decimal_number))
