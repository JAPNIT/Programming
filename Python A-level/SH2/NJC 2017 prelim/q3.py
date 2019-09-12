class BSTNode():
    def __init__(self,data):
        self._data = data
        self._left = None
        self._right = None

    def get_data(self):
        return self._data
    def set_data(self,x):
        self._data = x

    def get_left(self):
        return self._left
    def get_right(self):
        return self._right

    def set_left(self,x):
        self._left = x
    def set_right(self,x):
        self._right = x

    def print(self):
        print(self._data)

class LLNode(BSTNode):
    def __init__(self,data):
        super().__init__(data)
        self._next = None

    def get_next(self):
        return self._next
    def set_next(self,x):
        self._next = x

class HybridStructure():
    def __init__(self):
        self._first = None

    def get_first(self):
        return self._first
    def set_first(self,x):
        self._first = x

    def equal(self,a,b):
        a %= 100
        a //= 10
        b %= 100
        b //= 10
        if a == b:
            return True
        return False

    def inLL(self,x):
        current = self._first
        while current != None:
            if self.equal(int(current.get_data()),int(x)):
                return True
            current = current.get_next()
        return False

    def insert(self,x):
        #empty
        if self._first == None:
            self._first = LLNode(x)

        #not in ll
        
        elif not self.inLL(x):
            print("in here",x)
            current = self._first
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(LLNode(x))

        #in ll - add to bst
        else:
            current = self._first
            while not self.equal(int(current.get_data()),int(x)):
                current = current.get_next()
            while True:
                if current.get_data() < x:
                    if current.get_right() == None:
                        current.set_right(BSTNode(x))
                        break
                    else:
                        current = current.get_right()
                else:
                    if current.get_left() == None:
                        current.set_left(BSTNode(x))
                        break
                    else:
                        current = current.get_left()
                        
    def contains(self,x):
        current = self._first
        while not self.equal(int(current.get_data()),int(x)):
                current = current.get_next()
        while True:
            if current.get_data() < x:
                if current.get_right() == None:
                    return False
                else:
                    current = current.get_right()
                    
            elif current.get_data() == x:
                return True
                
            else:
                if current.get_left() == None:
                    return False
                else:
                    current = current.get_left()
        
    def inorder(self,x):
        if x:
            self.inorder(x.get_left())
            x.print()
            self.inorder(x.get_right())
            
    def print(self):
        current = self._first
        while current != None:
            self.inorder(current)
            print()
            current = current.get_next()


hs = HybridStructure()
hs.insert(15)
#hs.print()
hs.insert(12)
#hs.print()
hs.insert(16)
#hs.print()
hs.insert(18)
#hs.print()
hs.insert(45)
#hs.print()

hs.insert(44)
#hs.print()
hs.insert(55)
#hs.print()
hs.insert(98)
#hs.print()
hs.insert(97)

hs.insert(94)
hs.print()


            
