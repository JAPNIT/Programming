#4:45 -
class ListNode():
    def __init__(self):
        self._DataValue = ""
        self._PointerValue = None

    def getdata(self):
        return self._DataValue
    def getnext(self):
        return self._PointerValue

    def setdata(self,x):
        self._DataValue = x
    def setnext(self,x):
        self._PointerValue = x

class LinkedList():
    def __init__(self):
        self._Node = [ListNode() for i in range(31)]
        for i in range(1, 30):
            self._Node[i].setnext(i+1)
        self._Node[30].setnext(0)
        
        self._Start = 0
        self._NextFree = 1


    def IsEmpty(self):
        if self._Start == 0:
            return True
        return False

    def IsFull(self):
        if self._NextFree == 0:
            return True
        return False

    def AddNode(self,data):
        print("adding")
        print(data)
        self._Node[self._NextFree].setdata(data)
        index = self._NextFree
        self._NextFree = self._Node[self._NextFree].getnext()

        #empty:
        if self.IsEmpty():
            self._Start = index
            self._Node[index].setnext(0)

        else:
            #first:
            if data < self._Node[self._Start].getdata():
                self._Node[index].setnext(self._Start)
                self._Start = index

            else:
                current = self._Node[self._Start]
                while data > self._Node[current.getnext()].getdata() and current.getnext() != 0:
                    current = self._Node[current.getnext()]

                
                self._Node[index].setnext(current.getnext())
                current.setnext(index)

    def Display(self):
        print(self._Start)
        print(self._NextFree)

        print("LL")
        current = self._Start
        while current != 0:
            print(str(self._Node[current].getdata()) + " " + str(current)\
                  + " " + str(self._Node[current].getnext()))
            current = self._Node[current].getnext()

        print()

        print("Array")
        for i in self._Node:
            if i.getdata() != "":
                print(i.getdata())
        

                
ll = LinkedList()

while True: 
    print("1. Add an item")
    print("2. Traverse the linked list of used nodes and output datavalues")
    print("3. Output all pointer and data values")
    print("5. Exit")
    choice = input("Enter choice: ")
    

    

    if choice == "1":
        x = input("Enter value: ")
        ll.AddNode(x)
    elif choice == "2":
        pass
    elif choice == "3":
        ll.Display()
    elif choice == "5":
        break
    else:
        print("Please enter a valid input")
    
