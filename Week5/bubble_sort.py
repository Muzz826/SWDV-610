# Developed by: Ben Muzzy
# Code structure used from course Module 5 bubble sort example


def bubble_sort(seq):
# keeps track of number of times inner loops should repeat
    for num in range(len(seq)-1, 0, -1):
# no swaps occur if 2 neighboring items are in the right order
        for index in range(num):
# stores the larger value in front of the list in a temp location
            if seq[index] > seq[index +1]:
                temp = seq[index]
# swaps the neighboring item to the front of the list
                seq[index] = seq[index +1]
        # number in temp location now where the adject item was
                seq[index + 1] = temp
    print(seq)


bubble_sort([10, 2, 9, 5, 7, 1, 3, 8, 4, 6])
