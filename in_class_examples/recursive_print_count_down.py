def print_count_down(number):
    if number == 0:
        print(0)
    else:
        print(number)
        print_count_down(number-1)


print_count_down(5)
