class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
  
    def append(self, data):
        node = Node(data)
        
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def traverse(self):
        node = self.head
        
        while node:
            val = node.data
            node = node.next
            yield val
    
    def find_size(self):
        count = 0
        for i in self.traverse():
            count += 1
        return count
    
    def make_list(self):
        lst = []
        for i in self.traverse():
            lst.append(i)
        
        return lst


