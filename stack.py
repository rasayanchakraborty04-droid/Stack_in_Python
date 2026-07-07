# Stack implementation using linked list

# Class to create a fresh Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    # Add a new element to the top of the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    # Remove and return the top element of the stack
    def pop(self):
        if self.top == None:
            raise IndexError("Stack is empty")
        value = self.top.data
        self.top = self.top.next
        self.length -= 1
        return value

    # Return the top element of the stack without removing it
    def peek(self):
        if self.top == None:
            raise IndexError("Stack is empty")
        return self.top.data
    
    # Check if the stack is empty
    def in_empty(self):
        return self.top is None

    # Return the number of elements in the stack
    def size(self):
        return self.length    

