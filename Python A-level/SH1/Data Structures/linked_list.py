class LLnode():
    def __init__(self,value):
        self._value = value
        self._next = None

    def get_data(self):
        return self._value
    def set_data(self,new_value):
        self._value = new_value

    def get_next(self):
        return self._next
    def set_next(self,new_next):
        self._next = new_next

    def __str__(self):
        return self._value
    
class Linked_list():
    def __init__(self):
        self._first = None

    def print_list(self):
        if self._first == None:
            print("None")
        current = self._first
        while current != None:
            print(current.get_data())
            current = current.get_next()

    def insert_back(self,value):
        new_node = LLnode(value)
        if self._first == None:
            self._first = new_node
        else:
            current = self._first
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)

    def insert_first(self,value):
        new_node = LLnode(value)
        new_node.set_next(self._first)
        self._first = new_node

    def exist(self,value):
        if self._first == None:
            return 0
        current = self._first
        while current != None:
            if current.get_data() == value:
                return 1
            current = current.get_next()
        return 0
        

    def delete(self,value):
        if self._first == None:
            return 0
        current = self._first
        while current.get_next() != None:
            if current.get_next().get_data() == value:
                current.set_next(current.get_next().get_next())
                return 1
            current = current.get_next()
        return 0

    
            
        
LL = Linked_list()
LL.insert_back(10)
LL.insert_back(5)
LL.insert_first(6)
LL.insert_first(7)
LL.insert_first(8)
LL.print_list()
print("---")
print(LL.delete(5))
print(LL.delete(10))
LL.print_list()
print(LL)
