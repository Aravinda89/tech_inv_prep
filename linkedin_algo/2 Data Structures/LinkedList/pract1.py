
# Node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_val(self):
        return self.val
    
    def get_next(self):
        return self.next

    def set_val(self, val):
        self.val = val

    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self, head):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert_item(self):
        


