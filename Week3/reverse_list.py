# This app will take a sequence of numbers and
# reverse their by using recusion
# Developed by: Ben Muzzy

# sequence of numbers that will be reversed
seq = "987654321"


def ReverseList(seq):
    # Runs through the list until the list is empty
    if len(seq) < 1:
        return seq
    else:
    # Each pass the function makes it moves whatever
    # the current first number is to the end.
    # Once the list is empty the list is displayed in reverse order.
        return ReverseList(seq[1:]) + seq[0]


print("This app takes a sequence of numbers and reverses their order:\n\n")
print("Original order: " + seq)
print("\nReverse Order: " + ReverseList(seq))
