class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
            self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        if index <0 or index > self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def delete(self,index):
        if self.head is None:
            raise IndexError("List is empty")
        
        if index <0 or index > self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next

        current = self.head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.length -= 1

    def search(self, data):
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                return position
        current = current.next
        position += 1

        raise ValueError("Data not found in the list")

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

    def size(self):
        return self.length