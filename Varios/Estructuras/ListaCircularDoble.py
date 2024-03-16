class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_list(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node

    def create_link(self, new_node):
        self.tail.next = new_node
        self.head.prev = new_node
        new_node.next = self.head
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.create_list(data)
        else:
            self.create_link(new_node)
            self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.create_list(data)
        else:
            self.create_link(new_node)
            self.head = new_node
