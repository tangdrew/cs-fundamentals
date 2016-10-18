# Queues
A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is a collection of entities that are kept in order and the only operations are to add an element to the end of the queue (enqueue) and to remove an element from the beginning of the queue (dequeue). Queues are often implemented as linked lists.

### Operation Complexity
Operation | Complexity 
--- | --- 
Enqueue|Θ(1)
Dequeue|Θ(1) if you have a pointer to last element, Θ(n) otherwise

### Classes Implemented
 - `Queue(head):` takes a linked list and provides queue operations

### Methods Implemented
 - `enqueue(node):` adds the node to the end of the queue
 - `dequeue():` removes and returns first node of the queue