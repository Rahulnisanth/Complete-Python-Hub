# USER DEFINED LINKED-LIST USING .py :
class Node:
    def __init__(self, data = None):
        self.value = data
        self.next = None
    
    def is_empty(self):
        return self.value is None
    
    def append(self, data):
        if self.is_empty():
            self.value = data
        elif self.next is None:
            self.next = Node(data)
        else:
            self.next.append(data)
        return 
    
    def insert(self, data):
        if self.is_empty():
            self.value = data
        else:
            new_node = Node(data)
            # Exchange the nodes of self & newNode :
            (self.value, new_node.value) = (new_node.value, self.value)
            (self.next, new_node.next) = (new_node.next, self.next)

    def delete(self,data):
        if self.is_empty():
            return
        if self.value == data:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
        elif self.next is not None:
            self.next.delete(data)
            if self.next.value is None:
                self.next = None
        return
    
    def print_list(self):
        lst = []
        if self.value is None:
            return lst
        
        temp = self
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        return lst



    
