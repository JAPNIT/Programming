"""
UML Class Diagram
Class name: Linked lists
+/- Attributes (+ ~ public)
-LLnode
+/- Methods (- ~ public)
+initialisation()
+insert(object)
+delete(object):bool
+exist(object):bool
+count
+print

Class name: LLNode
+/- Attributes
-Object
-LLNode
+/- Methods
+initialisation
+get/set

LLNode
def __str__(self):
    return str(self._data)

Linked list
def __str__(self):
    current = self._First
    while current != None:
        print(current)
        current = current.get_next()
"""
class linked_list():
    def __init__(self):
        self._first = None

    def insert_front(self,new_value):
        new_node = LL_node(new_value)
        if self._first == None:
            self._first = new_node
        else:
            new_node._link = self._first
            self._first = new_node

    def insert_back(self,new_value):
        new_node = LL_node(new_value)
        if self._first == None:
            self._first = new_node
        else:
            current = self._first
            while True:
                if current.get_next() == None:
                    break
                current = current.get_next()
            current.set_next(new_node)

    def exist(self,val):
        current = self._first
        while True:
            if current.get_val() == val:
                return 1
            if current.get_next() == None:
                return 0
            current = current.get_next()        

    def delete(self,val):
        if self._first == None:
            return 0
        current = self._first
        prev = None
        while True:
            if current.get_val() == val:
                if prev:
                   prev.set_next(current.get_next())
                else:
                    self._first = current.get_next()
                return 1
            if current.get_next() == None:
                print("Value not found")
                return 0
            prev = current
            current = current.get_next()
                
    def print_list(self):
        current = self._first
        while current != None:
            print(current.get_val())
            current = current.get_next()

class LL_node():
    def __init__(self,value):
        self._value = value
        self._link = None

    def get_val(self):
        return self._value
    def get_next(self):
        return self._link

    def set_val(self,val):
        self._value = val
    def set_next(self,link):
        self._link = link


            
    
    
        
    

