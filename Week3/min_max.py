# This is a program that will display the minimum and maximum
# values of a given list (the list must be more than 1 value in length)
# Developed by: Ben Muzzy

def min_max(values, seq):
    # if list only has 1 value return that value as both the min & max values
    if seq == 1:
        return [values[0], values[0]]
    # if the list has more than one value return the min and max values
    else:
        (values)[seq - 1], min_max(values, seq - 1)
    return [min(values), max(values)]

def test(min_max):
    # list of values to find the min and max from
    values = [800]
    seq = len(values)
    results = (min_max(values, seq))
    print("minimum value is:", results[0], "maximum value is:", results[1])

test(min_max)