""" To find fibonacci series using given values upto choosen range """


def fibonacciSeries(x_value, y_value, max_range):
    fibonacci_List = []
    z_value = 0
    while z_value < max_range:
        z_value = x_value + y_value
        if z_value < max_range:
            fibonacci_List.append(z_value)
            x_value = y_value
            y_value = z_value

    print(fibonacci_List)


x_value = int(input("Enter x_value : "))
y_value = int(input("Enter y_value : "))
max_range = int(input("Enter max_range : "))
fibonacciSeries(x_value, y_value, max_range)