"""For data analysis in data science"""

def main():
    """gets data list/set"""
    user_input = (input("Enter the list of numbers separated by a space:"))
    data_set = list(map(int, user_input.split(" ")))
    print(data_set)
    minimum = find_minimum(data_set)
    maximum = find_maximum(data_set)
    data_range = find_range(minimum, maximum)
    print("Min = {}\nMax = {}\nRange = {}".format(minimum, maximum, data_range))


def find_minimum(data):
    """finds the min value in the data set"""
    minimum_of_set = min(data)
    return minimum_of_set


def find_maximum(data):
    """finds the max value in the data set"""
    minimum_of_set = max(data)
    return minimum_of_set


def find_range(low, high):
    """finds the range of the data set"""
    difference = high - low
    return difference


main()
