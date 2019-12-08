# This program takes two integer values and returns True if n is a multiple of m and False otherwise.
# Developed by: Ben Muzzy

def is_multiple(n, m):
    # divides n by m and checks if there is a remainder
    if n % m == 0:
    # if no remainder than the statement is true
        print("True")
    else:
    #if there is a remainder the statment is false.
        print("False")

is_multiple(15, 3)