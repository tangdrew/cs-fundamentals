# Stacks
A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a collection of elements with two principal operations: push, which adds an element to the collection, and pop, which removes the most recently added element. Can be thought of as a LIFO queue.



### Operation Complexity
Operation | Complexity 
--- | --- 
Push|Θ(1) with a pointer to the last (top) element
Pop|Θ(1) with a pointer to the last (top) element

### Classes Implemented
 - `Stack(head):` takes a node and provides stack operations

### Methods Implemented
 - `push(node):` adds node to the top of the stack
 - `pop():` removes and returns the top node of the stack