""" To find whether given number is armstrong number or not """


def armstrong_Number(input_Number):
    length_of_inputNumber = len(str(input_Number))
    result_Number = 0
    original_Number = input_Number

    while input_Number > 0:
        updated_Number = input_Number % 10
        result_Number += updated_Number ** length_of_inputNumber
        input_Number //= 10

    if result_Number == original_Number:
        print("Armstrong number")
    else:
        print("Not a Armstrong number")


number = int(input("Enter a number to check armstrong condition:"))
armstrong_Number(number)
