"""doctest example"""

import doctest


def get_middle(values):
    """
    Finds the middle value of a list.
    >>> get_middle([1, 2])
    1
    >>> get_middle([1, 2, 3])
    2
    >>> get_middle("abc")
    'b'
    """
    mid_value = round((len(values) - 1)/2)
    return values[mid_value]


doctest.testmod()

print(get_middle([1, 2]))
assert get_middle([1, 2]) == 1
