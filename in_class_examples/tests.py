def is_odd(number):
    return number % 2 == 1


assert is_odd(3)
print("Test: is_odd(3)\nExpected: True")
print("Got     : " + str(is_odd(3)))

assert not is_odd(4)
print("Test: is_odd(4)\nExpected: False")
print("Got     : " + str(is_odd(4)))

