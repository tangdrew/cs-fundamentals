# Linked Lists

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is a linear collection of data elements (nodes), each pointing to the next.

### Types of Linked Lists
 - [x] Singly Linked List
 - [ ] Doubly Linked List
 - [ ] Circular Linked List

### Operation Complexity
Operation | Complexity 
--- | --- 
Indexing|Θ(n)
Insert/delete at beginning|Θ(1)
Insert/delete at end|Θ(n) when last element unknown; Θ(1) when last element known
Insert/delete in middle|search time + Θ(1)
Wasted space (average)|Θ(n)

### Classes Implemented
 - `Node(data, next):` data stored at node, next points to another node

### Methods Implemented
 - `print_linked_list():` prints all the nodes of the linked list starting from the node to the console in form "a -> b -> c"
