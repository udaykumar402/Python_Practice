""" To check whether the given string is palindrome or not """


# Method_1
def palindrome(string):
    rev_string = string[::-1]
    if rev_string == string:
        print(string, "is a palindrome")


palindrome("ABA")


# Method_2
def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


string = "ABA"
print(f"{string} is a palindrome: {is_palindrome(string)}")
