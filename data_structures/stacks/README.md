# Stacks
A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a collection of elements with two principal operations: push, which adds an element to the collection, and pop, which removes the most recently added element. Can be thought of as a LIFO queue.
![alt text](https://en.wikipedia.org/wiki/File:Lifo_stack.png "Stack representation")


### Operation Complexity
Operation | Complexity 
--- | --- 
Enqueue|Θ(1)
Dequeue|Θ(1) if you have a pointer to last element, Θ(n) otherwise

### Classes Implemented
 - `Queue(head):` takes a linked list and provides queue operations

### Methods Implemented

### Examples Implemented
 - `fifo_queue` first-in-first-out queue as a linked list a -> b -> c