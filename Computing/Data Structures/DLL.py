class DLLNode():
    def __init__(self,  new_data):
        self._data = new_data
        self._prev = None
        self._next = None
    def get_data(self):
        return self._data
    def get_prev(self):
        return self._prev
    def get_next(self):
        return self._next
    def set_data(self, new_data):
        self._data = new_data
    def set_prev(self, new_prev):
        self._prev = new_prev
    def set_next(self, new_next):
        self._next = new_next
    def __str__(self):
        return str(self._data)

class DLL():
    def __init__(self):
        self._first = None
    def exists(self, target):
        if self._first == None:
            return False
        current = self._first
        while current.get_next() != None and current.get_data() != target:
            current = current.get_next()
        if current.get_data() == target:
            return True
        else:
            return False
    def insert_front(self, new_data):
        new_node = DLLNode(new_data)
        if self._first != None:
            new_node.set_next(self._first)
            self._first.set_prev(new_node)
        self._first = new_node
    def insert_back(self, new_data):
        new_node = DLLNode(new_data)
        if self._first == None:
            self._first = new_node
        else:
            last_node = self._first
            while last_node.get_next() != None:
                last_node = last_node.get_next()
            last_node.set_next(new_node)
            new_node.set_prev(last_node)
    def delete(self, target):
        if self._first == None:
            return False
        current = self._first
        while current.get_next() != None and current.get_data() != target:
            current = current.get_next()
        if current.get_data() == target:
            if current.get_prev() == None:
                self._first = current.get_next()
            else:
                current.get_prev().set_next(current.get_next())
            if current.get_next() != None:
                current.get_next().set_prev(current.get_prev())
            return True
        else:
            return False
    def __str__(self):
        s = "List Contents: ["
        current = self._first
        while current != None:
            s += str(current.get_data())
            if current.get_next() != None:
                s += ", "
            current = current.get_next()
        s += "]"
        return s
        
# Testing
my_list = DLL()
print("List after initialisation: " + str(my_list))
print("")
for i in range(10, 0, -1):
    my_list.insert_front(i)
print("List after insert_front calls: " + str(my_list))
print("")
print("Deleting " + str(5) + " from list: " + str(my_list.delete(5)))
print("List after deletion above: " + str(my_list))
for i in range(0, 12):
    print("Deleting " + str(i) + " from list: " + str(my_list.delete(i)))
    print("List after deletion above: " + str(my_list))
print("")
for i in range(1, 11):
    my_list.insert_back(i)
print("List after insert_front calls: " + str(my_list))
print("")
for i in range(10, 0, -1):
    print("\tDeleting " + str(i) + " from list: " + str(my_list.delete(i)))
    print("List after deletion above: " + str(my_list))













        

        
