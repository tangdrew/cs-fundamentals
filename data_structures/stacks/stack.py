import sys
sys.path.append('../')

from data_structures.linked_lists.linked_list import *

##### Class definitions #####
class Stack():
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def pop(self):
        head = self.head
        self.head = self.head.next
        return head

    def peek(self):
        return self.head.data

    def __str__(self):
        if self.head == None:
            return "~empty stack~"
        return self.head.print_linked_list()
    
##### Method definitions #####


##### Testing #####
def stack_test():
    print("=====Stack Testing=====")
    s = Stack()
    print("Empty stack:")
    print(s)
    s.push(Node("a"))
    print("Single element stack:")
    print(s)
    s.push(Node("b"))
    s.push(Node("c"))
    print("Push two nodes:")
    print(s)
    print("Peek:")
    print(str(s.peek()))
    print("Pop:")
    s.pop()
    print(s)