""" To swap list elements without using 3rd variable """


def swap_list_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


my_list = [1, 2, 3, 4]
print("Before swapping:", my_list)
swap_list_elements(my_list, 1, 2)
print("After swapping:", my_list)