#3:30 - 4:26
class ListNode():
    def __init__(self):
        self._Name = ''
        self._Pointer = None

    def SetName(self,Name):
        self._Name = Name
    def SetPointer(self,Pointer):
        self._Pointer = Pointer

    def GetName(self):
        return self._Name
    def GetPointer(self):
        return self._Pointer

class LinkedList():
    def __init__(self):
        self._Node = [ListNode() for i in range(11)]
        self._Start = 0
        self._NextFree = 1

    def Create(self):
        for i in range(1,10):
            self._Node[i].SetPointer(i+1)
        self._Node[10].SetPointer(0)

    def Length(self):
        current = self._Start
        count = 0
        while current != 0:
            count += 1
            current = self._Node[current].GetPointer()
        return count 

    def IsEmpty(self):
        if self.Length == 0:
            return True
        return False

    def IsFull(self):
        if self.Length == 10:
            return True
        return False

    def Insert(self,data,p):
        self._Node[self._NextFree].SetName(data)
        index = self._NextFree
        self._NextFree = self._Node[self._NextFree].GetPointer()

        if self._Start == 0:
            self._Start = index
            self._Node[index].SetPointer(0)

        elif p == 1:
            self._Node[index].SetPointer(self._Start)
            self._Start = index

        else:
            current = self._Node[self._Start]
            for i in range(p-2):
                current = self._Node[current.GetPointer()]
            prev = current
            self._Node[index].SetPointer(current.GetPointer())
            prev.SetPointer(index)
            
    def Delete(self,p):
        if p == 1:
            index = self._Start
            self._Start = self._Node[self._Start].GetPointer()
            
            
        else:
            current = self._Node[self._Start]
            for i in range(p-2):
                current = self._Node[current.GetPointer()]
            prev = current
            index = prev.GetPointer()
            prev.SetPointer(self._Node[prev.GetPointer()].GetPointer())
            
        self._Node[index].SetName('')
        self._Node[index].SetPointer(self._Node[self._NextFree].GetPointer())
        self._NextFree = index

    def Display(self):
        current = self._Start
        print(current)
        print(self._NextFree)
        while current != 0:
            print(self._Node[current].GetName())
            current = self._Node[current].GetPointer()
        print()
        print("Array")
        for i in self._Node:
            if i.GetName() == "":
                print(None)
            else:
                print(i.GetName())
            
l = LinkedList()
l.Create()
print("length")
print(l.Length())
l.Insert('Ali',1)
l.Display()
print("length")
print(l.Length())
l.Insert('Jack',1)
l.Display()
print("length")
print(l.Length())
l.Insert('Ben',2)
l.Display()
print("length")
print(l.Length())
l.Delete(1)
l.Display()
print("length")
print(l.Length())
l.Insert('Jane',2)
l.Display()
print("length")
print(l.Length())
l.Insert('Ken',3)
l.Display()
print("length")
print(l.Length())
l.Delete(2)
l.Display()
print("length")
print(l.Length())


class q(LinkedList):
    def __init__(self):
        super().__init__()
        self.head = 0
        self.tail = 0

    def enq(self,data):
        self._Node[self.tail].SetName(data)
        self.tail += 1

    def dq (self):
        self._Node[self.head].SetName('')
        self.head +=1

    def Display(self):
        index = self.head
        while True:
            if index == self.tail:
                break
            if abs(self.head-self.tail) == 1:
                print(str(self._Node[index].GetName()) + "    <- Front and Back")
            elif index == self.head:
                print(str(self._Node[index].GetName()) + "    <- Front")
            elif index == self.tail-1:
                print(str(self._Node[index].GetName()) + "    <- Back")
            else:
                print(str(self._Node[index].GetName()))
            index += 1
        print()
            
                
q = q()
q.Create()
q.enq("hi")
q.Display()
q.enq("hi")
q.Display()
q.enq("hi")
q.Display()
q.dq()
q.Display()
q.enq("hi")
q.Display()
q.dq()
q.Display()
            
        
