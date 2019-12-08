# Developed by: Ben Muzzy
# Code structure used from course Module 5 selection sort example


def insertion_sort(seq):
# starts at index 1 because sub-array at index 0 assumed to be already sorted
    for index in range(1, len(seq)):
        find = index
# curr_val stores the item at seq[index] until the position in the sorted portion of the list is found
        curr_val = seq[index]
        while find > 0 and seq[find -1] > curr_val:
        # swaps item down the list
            seq[find] = seq[find -1]
            find -= 1
        # Break and performs final swap
        seq[find] = curr_val
    print(seq)


insertion_sort([10, 2, 9, 5, 7, 1, 3, 8, 4, 6])
