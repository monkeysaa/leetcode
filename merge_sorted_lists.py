class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        """Initialize a linked list"""

        self.head = None
        self.tail = None

    def append(self, node):
        """Append an existing node"""
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
    
    def clear(self):
        self.head = None
        self.tail = None
    
    def traverse(self):

        curr = self.head

        while curr:
            value = curr.val
            curr = curr.next
            yield value
    
    def length(self):

        count = 0
        for i in self.traverse():
            count += 1
        
        return count

    
    def print_list(self):

        for i in self.traverse():
            print(i)

# convert_to_array(self):
    # self.list = []
    #     for i in self.traverse():
    #         self.list.append(i)
    #     return self.list

# WHAT'S WRONG WITH THIS FUNCTION? 
# What would be a better way to build an array for this LinkedList? Why? 
# What are the pros and cons of creating a new list each time vs. caching a list?
    # How would each impact memory?
    # How would each impact performance?

def mergeTwoLists(node1, node2):
    """Given in head nodes of 2 sorted singly-linked lists, merge lists."""
    
    new_list = LinkedList()

    import pdb; pdb.set_trace()
    while node1 and node2:
        if node1.val >= node2.val:
            new_list.append(node2)
            node2 = node2.next
        else:
            new_list.append(node1) 
            node1 = node1.next
    
    if node1 is None:
        new_list.append(node2)

    elif node2 is None:
        new_list.append(node1)
    
    return new_list.head

print('hello')
ll = LinkedList()
ll2 = LinkedList()
ll.append(ListNode(1))
ll.append(ListNode(5))
ll.append(ListNode(6))
ll2.append(ListNode(1))
ll2.append(ListNode(2))
ll2.append(ListNode(4))
ll2.append(ListNode(8))
print(mergeTwoLists(ll.head, ll2.head))

# answer = mergeTwoLists(ll.head, ll2.head)
# print(answer)
# Whereas Line 94 works fine, Line 95 creates an infinite loop. 
# BUT THEY'RE THE SAME CODE?!...right?  Please explain.
