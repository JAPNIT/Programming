#1:51 - 2:20
class Node():
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def getdata(self):
        return self._data
    def getnext(self):
        return self._next
    def getprev(self):
        return self._prev

    def setnext(self, x):
        self._next = x
    def setdata(self,x):
        self._data = x
    def setprev(self,x):
        self._prev = x

class CDLL():
    def __init__(self):
        self._head = None
        self._last = None
        self._size = 10
        self._count = 0

    def isEmpty(self):
        if self._head == None:
            return True
        return False

    def isFull(self):
        if self._count == self._size:
            return True
        return False

    def insertfront(self,data):
        newnode = Node(data)

        if self.isFull():
            print("Full")

        if self.isEmpty():
            self._head = newnode
            self._last = self._head
            self._last.setnext(self._head)
            self._head.setprev(self._last)
            

        else:
            temp = self._head
            self._head = newnode
            self._head.setnext(temp)
            temp.setprev(self._head)
            self._last.setnext(self._head)
            self._head.setprev(self._last)

    def insertback(self,data):
        newnode = Node(data)

        if self.isFull():
            print("Full")

        if self.isEmpty():
            self.insertfront(data)

        else:
            temp = self._last
            self._last = newnode
            temp.setnext(self._last)
            self._last.setprev(temp)
            self._last.setnext(self._head)
            self._head.setprev(self._last)

    def delete(self, data):
        current = self._head
        if current.getdata() == data:
            self._head = self._head.getnext()
            self._last.setnext(self._head)
            self._head.setprev(self._last)

        else:
            while True:
                if current.getdata() == data:
       
                    if current != self._last:
                        prev = current.getprev()
                        after = current.getnext()
                        prev.setnext(after)
                        after.setprev(prev)
                        
                    else:
                        prev = current.getprev()
                        self._last = prev
                        self._last.setnext(self._head)
                        self._head.setprev(self._last)
                    break 
                if current == self._last:
                    break
                current = current.getnext()
                        
                    
                    

    def sortHelper(self, a):
        for i in range(1,len(a)):
            j = i
            while j > 0 and a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                j -= 1
        return a

    def sort(self,data):
        current = self._head
        contents = []
        while current != None:
            contents.append(current.data)
            current = current.getnext()
        contents = self.sortHelper(contents)
        print("sorted")
        print(contents)

        for i in contents:
            self.delete(i)
        for i in contents:
            self.insertBack(i)

    def exists(self,data):
        current = self._head
        while True:
            if current.getdata() == data:
                return True
            if current == self.last:
                return False
            current = current.getnext()

    def print(self):
        print(self._last.getnext().getdata())
        print(self._head.getprev().getdata())
        
        print("forward")
        current = self._head
        while True:
            print(current.getdata())
            if current == self._last:
                break
            current = current.getnext()

        print("backward")
        current = self._last
        while True:
            print(current.getdata())
            if current == self._head:
                break
            current = current.getprev()
            
            
print("circular DLL")                      
ll = CDLL()
ll.insertback(3)
ll.print()
print("--")
ll.insertback(4)
ll.print()
print("--")
ll.insertfront(9)
ll.print()
print("--")
ll.insertfront(10)
ll.print()
print("--")
ll.insertfront(11)
ll.print()
print("--")
ll.delete(11)
ll.print()
print("--")
ll.delete(9)
ll.print()
print("--")
ll.delete(4)
ll.print()
print("--")                     
                
        


        
            
            
        
            










        
        
    
        
