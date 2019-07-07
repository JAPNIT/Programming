class Square():
    def __init__(self, length):
        self._length = length

    def getLength(self):
        return self._length

    def computePerimeter(self):
        return 4*self.getLength()

    def computeArea(self):
        return pow(self.getLength(), 2)

class Rectangle(Square):
    def __init__(self,length, breadth):
        super().__init__(length)
        self._breadth = breadth

    def getBreadth(self):
        return self._breadth

    def computePerimeter(self):
        return 2*self.getLength() + 2*self.getBreadth()

    def computeArea(self):
        return self.getLength() * self.getBreadth()
    
sq = Square(5)
rect = Rectangle(5,10)
print(sq.computePerimeter())
print(sq.computeArea())
print(rect.computePerimeter())
print(rect.computeArea())
