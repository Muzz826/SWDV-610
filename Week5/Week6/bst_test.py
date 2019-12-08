from binary_search_tree import BinarySearchTree
from random import randint
# Developed by Ben Muzzy

bst = BinarySearchTree()
# will store the random numbers generated
seq = []
#start at zero instead of 1
key = 0

print("Keys and random values for Binary Search Tree:")
# This loop will generate 5 random numbers between 1 and 1000
for index in range(5):
    seq.append(randint(1, 1000))
    bst.put(key, seq[index])
    # each number generated will get correpsonding key to go with it.
    print(key, seq[index])
    key += 1
    
# prints a random list of numbers from the above for statement
print()

#prints the binary tree
print("Print Tree:")
bst.printtree()

print("\n")


#shows traversing the tree (navigating the tree)
print("Traverse Tree:")
bst.traverse()
