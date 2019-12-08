# This program is an example of a stack using a linked list.
# Developed by: Ben Muzzy

# Structure of node taken from
# week 4 module.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Looks for the next node
    def get_next(self):
        return self.next


# Used to created the stack (list in first out).
class Stack:
    def __init__(self):
        self.head = None

    # Checks to see if the stack is empty
    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        return self.size

    # Push adds data to the stack
    def push(self, data):
        # creates a new node on data insertion
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return "Successfully pushed cert " + data + " into the stack!\n"
        return self.stack

    # Pop removes data from the stack
    def pop(self):
        if self.is_empty():
            "The cert stack is empty!"
            return
        popped = self.head.data
        self.head = self.head.next
        return popped + " was removed from the stack.\n"

    # Peek is used to look at an data in the stack
    def peek(self):
        if self.is_empty():
            return "No certs are listed in the stack!"
        return self.head.data

    # Prints each node of the stack to display my certs
    def d_stack(self):
        current = self.head
        while current:
            print(current.data)
            current = current.get_next()


def main():
    cert = Stack()
    print(cert.push("A+"))
    print(cert.push("Network+"))
    print(cert.push("Security+"))
    print(cert.d_stack())
    print(cert.pop())
    print(cert.d_stack())
    print(cert.pop())
    print(cert.d_stack())
    print(cert.pop())
    print(cert.d_stack())  # None = no more nodes


main()
