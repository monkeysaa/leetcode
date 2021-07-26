class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_data(self, data):
        new_node = ListNode(data)
        if head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next == new_node
            self.tail = new_node

    def traverse_list(self, operate):
        if self.head is not None:
            current = self.head
            while current:
                operate(current.val)
                current = current.next
    
    ##### ASK ABOUT YIELD VARIANT #####
    # def traverse_list(self):
    #     if self.head:
    #         current = self.head
    #         while current:
    #             val = current.data
    #             current = current.next
    #             yield val