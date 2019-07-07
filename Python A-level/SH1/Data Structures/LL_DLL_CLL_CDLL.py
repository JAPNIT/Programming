#9.54 - 10.11 = 17
class Node():
    def __init__(self):
        self.data = None
        self.next = None

class LL():
    def __init__(self):
        self.head = None

    def newnode(self,data):
        newnode = Node()
        newnode.data = data
        return newnode

    def insertfront(self, data):
        newnode = self.newnode(data)
        temp = self.head
        self.head = newnode
        self.head.next = temp

    def insertback(self,data):
        newnode = self.newnode(data)

        #empty
        if self.head == None:
            self.head = newnode
            
        #not empty
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode

    def delete(self,data):
        
        if self.head == None:
            print("Empty")
            
        else:
            current = self.head

            #if its the head
            if current.data == data:
                temp = self.head.next
                self.head = temp

            else:
                while current.next != None:
                    if current.next.data == data:
                        current.next = current.next.next
                        break
                    current = current.next
                

    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
            
                    
ll = LL()
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

#10:15
class DLL_Node(Node):
    def __init__(self):
        super().__init__()
        self._prev = None

    def get_prev(self):
        return self._prev

    def set_prev(self,data):
        self._prev = data

class DLL(LL):
    def __init__(self):
        super().__init__()

    def newnode(self, data):
        newnode = DLL_Node()
        newnode.data = data
        return newnode 

    def insertfront(self, data):
        newnode = self.newnode(data)
        temp = self.head
        self.head = newnode
        newnode.next = temp
        temp.set_prev(newnode)

    def insertback(self,data):
        newnode = self.newnode(data)

        #empty
        if self.head == None:
            self.head = newnode
            

        #not empty
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = newnode
            newnode.set_prev(current)

    def delete(self, data):
        current = self.head
        
        if current.data == data:
            self.head = self.head.next
            self.head.set_prev(None)

        else:
            while current.next != None:
                if current.next.data == data:
                    
                    if current.next.next != None:
                        current.next = current.next.next
                        current.next.set_prev(current)

                    else:
                        current.next = current.next.next
                    break
                current = current.next
                
    def print(self):
        current = self.head
        
        print("forward")
        while current.next != None:
            print(current.data)
            current = current.next
        print(current.data)

        print("backwards")
        while current.get_prev() != None:
            print(current.data)
            current = current.get_prev()
        print(current.data)
        


print("DLL")                      
ll = DLL()
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

#11:15 - 11:45
class Circular_LL(LL):
    def __init__(self):
        super().__init__()
        self.last = None

    def insertfront(self,data):
        newnode = self.newnode(data)
        #empty:
        if self.head == None:
            self.head = newnode
            
            self.last = self.head
                        
            self.last = self.head
            self.last.next = self.head

        else:
            temp = self.head
            self.head = newnode
            self.head.next = temp

            temp_last = temp
            while temp_last.next != temp:
                temp_last = temp_last.next
            self.last = temp_last
            
            self.last.next = self.head

    def insertback(self, data):
        newnode = self.newnode(data)

        #empty:
        if self.head == None:
            self.insertfront(data)

        else:
            temp_last = self.head
            while temp_last.next != self.head:
                temp_last = temp_last.next
            self.last = temp_last
            
            self.last.next = newnode
            newnode.next = self.head
            self.last = newnode

    def delete(self, data):
        current = self.head

        #first node
        if current.data == data:
            temp_last = self.head
            while temp_last.next != self.head:
                temp_last = temp_last.next
            self.last = temp_last
            
            self.head = self.head.next

            
            
            self.last.next = self.head

        else:
            while current.next != None:
                if current.next.data == data:
                    #in the middle
                    if current.next.next != None:
                        current.next = current.next.next
                    #last
                    else:
                        temp_last = self.head
                        while temp_last.next != self.head:
                            temp_last = temp_last.next
                        self.last = temp_last
                        
                        self.last = current.next
                        self.last.next = self.head
                    break
                current = current.next
                
    def print(self):
        print(self.last.next.data)
        current = self.head.next
        while current != None:
            if current == self.head:
                break
            print(current.data)
            current = current.next
        
             
            
print("circular LL")                      
ll = Circular_LL()
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


#11:45        
class Circular_DLL(DLL):
    def __init__(self):
        super().__init__()
        self.last = None

    def insertfront(self, data):
        newnode = self.newnode(data)

        #empty
        if self.head == None:
            self.head = newnode

            self.last = self.head

            self.last.next = self.head
            self.head.set_prev(self.last)

        else:
            temp_last = self.head
            while temp_last.next != self.head:
                temp_last = temp_last.next
            self.last = temp_last
            
            temp = self.head
            self.head = newnode
            newnode.next = temp
            temp.set_prev(newnode)

            self.last.next = self.head
            self.head.set_prev(self.last)

    def insertback(self, data):
        newnode = self.newnode(data)

        #empty:
        if self.head == None:
            self.insertfront(data)

        else:
            temp_last = self.head
            while temp_last.next != self.head:
                temp_last = temp_last.next
            self.last = temp_last

            temp = self.last
            self.last = newnode
            temp.next = self.last
            self.last.set_prev(temp)
            self.last.next = self.head
            self.head.set_prev(self.last)

    def delete(self, data):
        #first node:
        current = self.head
        
        temp_last = self.head
        while temp_last.next != self.head:
            temp_last = temp_last.next
        self.last = temp_last

        if current.data == data:
            self.head = self.head.next
            self.head.set_prev(self.last)
            self.last.next = self.head

        else:
            while True:
                if current.next.data == data:
                    #mid
                    if current.next.next != self.head:
                        current.next = current.next.next
                        current.next.set_prev(current)
                    #last
                    else:
                        self.last = current
                        self.last.next = self.head
                        self.head.set_prev(self.last)
                    break

                if current == self.last:
                    break
                current = current.next

    def print(self):  
        print(self.last.next.data)
        print(self.head.get_prev().data)
        print("forward")
        current = self.head
        while True:
            print(current.data)
            if current.next == self.head:
                break
            current = current.next
        
        
        print("backwards")
        current = self.last
        while True:
            print(current.data)
            if current == self.head:
                break
            current = current.get_prev()
        
print("circular DLL")                      
ll = Circular_DLL()
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
                
        
            

            
            
            
            
            
        
