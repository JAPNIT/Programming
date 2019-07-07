#8.05
class Node():
    def __init__(self):
        self.data = None
        self.next = None

class LL():
    def __init__(self):
        self.head = None

    def add(self,data):
        newnode = Node()
        newnode.data = data
        
        if self.head == None:
            self.head = newnode

        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = newnode

    def delete(self,data):
        if self.head.data == data:
            self.head = self.head.next

        else:
            current = self.head
            
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


class Hashtable():
    def __init__(self):
        self.size = 10
        self.ht = [LL() for i in range(self.size)]

    def hashfunc(self,s):
        return len(s)

    def insert(self,s):
        index = self.hashfunc(s) % self.size
        self.ht[index].add(s)

    def delete(self,s):
        index = self.hashfunc(s) % self.size
        self.ht[index].delete(s)

    def print(self):
        for i in range(len(self.ht)):
            print(i)
            self.ht[i].print()

ht = Hashtable()
ht.insert("hhh")
ht.insert("jjjjjjjj")
ht.insert("lll")
ht.delete("hhh")
ht.print()

       
        
