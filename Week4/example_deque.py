# This program is an example of a stack using a linked list.
# Developed by: Ben Muzzy

# Structure of node taken from
# week 4 module.
# Code based on page 275 of Data Structures and Algorithms text
# Also referenced tutorials from Geeks for Geeks website/videos
class DoublyLinkedList:
    class Node:
        # Starts the node
        def __init__(self, data, prev, next):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # Checks the length of the deque
    def __len__(self):
        return self.size

    # Checks if the deque is empty
    def is_empty(self):
        return self.size == 0

    # inserts data between two nodes and returns the new node
    def insert_between(self, data, predecessor, successor):
        latest = self.Node(data, predecessor, successor)
        predecessor.next = latest
        successor.prev = latest
        self.size = self.size + 1
        return latest
    
    # deletes node
    def erase_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size = self.size - 1
        data = node.data
        node.prev = node.next = node.data = None
        return data


class DequeLinked(DoublyLinkedList):
    def begin(self):
        if self.is_empty():
            return "The deque is empty!"
        return self.head.next.data

    def end(self):
        if self.is_empty():
            return "The deque is empty!"
        return self.tail.prev.data

    def insert_begin(self, data):
        self.insert_between(
            data, self.head, self.head.next)

    def insert_end(self, data):
        self.insert_between(data, self.tail.prev,
                            self.tail)

    def remove_begin(self):
        if self.is_empty():
            return "The deque is empty!"
        return self.erase_node(self.head.next)

    def remove_end(self):
        if self.is_empty():
            return "The deque is empty!"
        return self.erase_node(self.tail.prev)

    def size_deque(self):
        return self.size

    def print_deque(self):
        print(f"{'='*5}Cert Deque{'='*5}")
        temp = self.head
        while temp is not None:
            if temp.data is None:
                temp = temp.next
            else:
                print(temp.data)
                temp = temp.next


# initialize deque
cert = DequeLinked()
# print size
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# add certs
cert.insert_begin('A+')
cert.insert_begin('Network+')
cert.insert_begin('Security+')
# print size
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# print deque
cert.print_deque()
# add cert to the end of the deque
print("\nAdding cert to the end of the deque.")
cert.insert_end('Cloud')
# print size
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# print deque
cert.print_deque()
# add cert to the front of the deque
print("\nAdding cert to the front of the deque.")
cert.insert_begin('Python Ninja')
# print size
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# print deque
cert.print_deque()
# remove cert from front of the deque
print("\nRemoving cert from the front deque.")
cert.remove_begin()
# print size
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# print deque
cert.print_deque()
# remove cert from the end of the deque
print("\nRemoving cert from end of deque.")
cert.remove_end()
# print size
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# print deque
cert.print_deque()
# remove remaining certs
print("\nRemoving all certs from deque.")
cert.remove_begin()
cert.remove_begin()
cert.remove_begin()
print(f"The size of the cert deque is currently: {cert.size_deque()}\n")
# demonstrating error on empty
print("\nRemoving an extra cert to return error.")
print(cert.remove_begin())
