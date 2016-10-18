import sys
sys.path.append('../')

from data_structures.linked_lists.linked_list import *

##### Class definitions #####
class Queue():
    def __init__(self, head = None):
        self.head = head
        self.last = head

    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        head = self.head
        self.head = head.next
        return head

    def peek(self):
        return self.head.data

    def __str__(self):
        if self.head == None:
            return "~empty queue~"
        return self.head.print_linked_list()

##### Testing #####
def queue_test():
    print("=====Queue Testing=====")
    q = Queue()
    print("Empty queue:")
    print(q)
    q.enqueue(Node("a"))
    q.enqueue(Node("b"))
    q.enqueue(Node("c"))
    print("Multiple element queue:")
    print(q)
    print("Peek:")
    print(str(q.peek()))
    n = Node("last", None)
    q.enqueue(n)
    print("Enqueue:")
    print(q)
    q.dequeue()
    print("Dequeue:")
    print(q)