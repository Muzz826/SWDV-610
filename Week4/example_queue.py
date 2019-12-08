# This program is an example of a stack using a linked list.
# Developed by: Ben Muzzy

# Structure of node taken from
# week 4 module.
# Also referenced tutorials from Geeks for Geeks website/videos


class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return repr(self.data)


    # start of Queue (first in first out)
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # returns size of the queue
    def __len__(self):
        return self.size

    # appending data to the queue
    def __repr__(self):
        queue_list = []
        head = self.head
        while head is not None:
            queue_list.append(repr(head))
            head = head.next
        return 'Cert Queue:[{}]'.format(", ".join(queue_list))

    # Checks if the queue is empty or not.
    def is_empty(self):
        return True if self.head is None else False

    def first(self):
        if self.is_empty():
            return "The cert stack is empty!"
        return self.head.data

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "The cert stack is empty!"
        popped = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped + " was removed from the queue.\n"

    def size_queue(self):
        return self.size


def main():
    # initialize certs
    cert = Queue()

    # print size
    print(f"The size of the cert queue is currently: {cert.size_queue()}\n")

    # add certs
    cert.enqueue("A+")
    cert.enqueue("Network+")
    cert.enqueue("Security+")

    # print size
    print(f"The size of the cert queue is currently: {cert.size_queue()}\n")
    print(cert)

    # remove cert from the queue
    print("\nRemoving one cert from the queue.")
    cert.dequeue()
    # print size
    print(f"The size of the cert queue is currently: {cert.size_queue()}")
    print(cert)

    # remove temaining certs from the queue
    print("\nRemoving remaining certs from the queue")
    cert.dequeue()
    cert.dequeue()

    # print size
    print(f"The size of the cert queue is currently: {cert.size_queue()}")
    print(cert)

    # remove cert from the queue and try to view first item
    print("\nRemoving one cert from the queue.")
    print(cert.dequeue())


main()
