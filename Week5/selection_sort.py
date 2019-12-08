# Developed by: Ben Muzzy
# Code structure used from course Module 5 selection sort example


def selection_sort(seq):
# outer loop to track num of times inner loop repeats
    for num in range(len(seq)):
        minimum = num
# inner loop begins its search for the smallest element
        for index in range(num + 1, len(seq)):
    # selects the smallest value
            if seq[index] < seq[minimum]:
                minimum = index
# Places the smallest val at the front of the sorted end of array
        seq[minimum], seq[num] = seq[num], seq[minimum]
    print(seq)


selection_sort([10, 2, 9, 5, 7, 1, 3, 8, 4, 6])




