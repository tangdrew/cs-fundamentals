##### Class definitions #####
class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
    
    def print_linked_list(self):
        node = self
        if node == None:
            return "~empty~"
        node_list = [node.data]
        while node.next != None:
            node_list.append(node.next.data)
            node = node.next
        return " -> ".join(map(str, node_list))
    
##### Testing #####
def linked_list_test():
    print("=====Linked List Testing=====")
    print("Single element linked list:")
    singly_linked_list = Node("a")
    singly_linked_list.print_linked_list
    print("Multiple element linked list:")
    singly_linked_list = Node("a", Node("b", Node("c", None)))
    singly_linked_list.print_linked_list