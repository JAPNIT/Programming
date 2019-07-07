#5:28
class Node():
    def __init__(self):
        self._data = None
        self._leftPtr = -1
        self._rightPtr = -1

    def setData(self, x):
        self._data = x
    def setRightPtr(self,x):
        self._rightPtr = x
    def setLeftPtr(self,x):
        self._leftPtr = x

    def getData(self):
        return self._data
    def getLeftPtr(self):
        return self._leftPtr
    def getRightPtr(self):
        return self._rightPtr

class Tree:
    def __init__(self):
        self._size = 10
        self._thisTree = [Node() for i in range(self._size)]
        self._root = -1
        self._nextfree = 0

    def add(self,data):
        index = self._nextfree
        self._thisTree[index].setData(data)
        self._nextfree += 1

        #empty
        if self._root == -1:
            self._root = index

        else:
            current = self._root
            left_flag = False
            while True:
                if data > self._thisTree[current].getData():
                    if self._thisTree[current].getRightPtr() == -1:
                        break
                    else:
                        current = self._thisTree[current].getRightPtr()
                else:
                    if self._thisTree[current].getLeftPtr() == -1:
                        left_flag = True
                        break
                    else:
                        current = self._thisTree[current].getLeftPtr()
                        
            if left_flag:
                self._thisTree[current].setLeftPtr(index)
            else:
                self._thisTree[current].setRightPtr(index)

    def print(self):
        for i in self._thisTree:
            print("left: " + str(i.getLeftPtr()))
            print("data: " + str(i.getData()))
            print("right: " + str(i.getRightPtr()))
        
BST = Tree()
BST.add("Tiger")
BST.add("Lemur")
BST.add("Bat")
BST.add("Yak")
BST.add("Ostrich")
BST.print()
BST.add("Maccaw")
BST.print()
            
                
                

        
        

    
