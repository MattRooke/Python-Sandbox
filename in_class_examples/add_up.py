def add_up(number):
    if number == 0:
        return 0
    return number + add_up(number - 1)


print(add_up(6))
