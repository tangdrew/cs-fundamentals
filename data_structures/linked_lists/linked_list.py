class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
    
lList = Node("a", Node("b", Node("c", None)))

def print_linked_list(head):
    node = head
    node_list = [node.data]
    while node.next != None:
        node_list.append(node.next.data)
        node = node.next
    print(" -> ".join(map(str, node_list)))

print_linked_list(lList)
