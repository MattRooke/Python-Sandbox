"""For data analysis in data science"""

from statistics import median


def main():
    """gets data set(list) and prints relevant information"""
    user_input = (input("Enter the list of numbers separated by a space:"))
    data_set = list(map(float, user_input.split(" ")))
    print("Input: {}".format(data_set))
    data_set = order_set(data_set)
    print("Sorted: {}".format(data_set))
    print("Values = {}".format(len(data_set)))
    minimum = find_minimum(data_set)
    maximum = find_maximum(data_set)
    data_range = find_range(minimum, maximum)
    mean = find_mean(data_set)
    median_value = find_median(data_set)
    print("Min = {}\nMax = {}\nRange = {}\nMean = {}\nMedian = {}".format(minimum, maximum, data_range, mean, median_value))


def find_minimum(data):
    """finds the min value in the data set"""
    minimum_of_set = min(data)
    return minimum_of_set


def find_maximum(data):
    """finds the max value in the data set"""
    minimum_of_set = max(data)
    return minimum_of_set


def find_range(minimum, maximum):
    """finds the range of the data set"""
    difference = maximum - minimum
    return difference


def order_set(data):
    """Orders data set from lowest to highest"""
    data_set = sorted(data)
    return data_set


def find_mean(data):
    """finds the average of the data set"""
    mean = sum(data) / len(data)
    return mean


def find_median(data):
    median_value = median(data)
    return median_value


main()
