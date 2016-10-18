import sys
sys.path.append('../')

from data_structures.linked_lists.linked_list import *

##### Class definitions #####
class Queue():
    def __init__(self, head = None):
        self.head = head

    def enqueue(self, node):
        node.next = self.head
        self.head = node

    def dequeue(self):
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None

    def peek(self):
        return self.head.data
    
##### Method definitions #####


##### Examples #####
fifo_queue = Queue(singly_linked_list)

##### Testing #####
q = Queue(singly_linked_list)
print(str(q.peek()))
n = Node("start", None)
q.enqueue(n)
print_linked_list(q.head)
q.dequeue()
print_linked_list(q.head)