"""
UML Class Diagram
Class name: Quadrilateral
+/- Attributes (+ ~ public)
-side_1 : float
-side_2 : float
-side_3 : float
-side_4 : float
+/- Methods (- ~ public)
+initialisation(float,float,float,float)

achieved:
modularity
polymorphism
code reuse
"""

class Quadrilateral():
    
    def __init__(self,side_1,side_2,side_3,side_4):
        if self.check_input(side_1):
            self._side_1 = side_1
        else:
            self._side_1 = None

        if self.check_input(side_2):
            self._side_2 = side_2
        else:
            self._side_2 = None

        if self.check_input(side_3):
            self._side_3 = side_3
        else:
            self._side_3 = None

        if self.check_input(side_4):
            self._side_4 = side_4
        else:
            self._side_4 = None


    def check_input(self,side):
        if type(side) == type(1.0) or type(side) == type(1):
            return True
        return False

    def get_side_1(self):
        return self._side_1
    def get_side_2(self):
        return self._side_2
    def get_side_3(self):
        return self._side_3
    def get_side_4(self):
        return self._side_4

    def set_side_1(self,new):
        if self.check_input(new):
            self._side_1 = new
    def set_side_2(self,new):
        if self.check_input(new):
            self._side_2 = new
    def set_side_3(self,new):
        if self.check_input(new):
            self._side_3 = new
    def set_side_4(self,new):
        if self.check_input(new):
            self._side_4 = new

    def perimeter(self):
        if self._side_1 == None or  self._side_2 == None or self._side_3 == None or self._side_4 == None:
            return None
        return self._side_1 + self._side_2 + self._side_3 + self._side_4

    def print_quad(self):
        print("Side 1:" + str(self._side_1))
        print("Side 2:" + str(self._side_2))
        print("Side 3:" + str(self._side_3))
        print("Side 4:" + str(self._side_4))
        print("Perimeter:" + str(self.perimeter()))

class Trapezium(Quadrilateral):
    def __init__(s1,s2,s3,s4,ps1,ps2,p):
        super().__init__(s1,s2,s3,s4)
        if self.check(ps1):
            self._ps1 = ps1
        else:
            self._ps1 = None

        if self.check(ps12):
            self._ps2 = ps2
        else:
            self._ps2 = None

        if self.check(p):
            self._p = p
        else:
            self._p = None

    def check_input(self,side):
        if type(side) == type(1.0) or type(side) == type(1):
            return True
        return False

    def area(self):
        return .5 * self._p * (self._ps1+self._ps2)

class Kite(Quadrilateral):
    def __init__(s1,s2,s3,s4,d1,d2):
        super().__init__(s1,s2,s3,s4)
        if self.check_input(d1):
            self._d1 = d1
        else:
            self._d1 = None

        if self.check_input(d2):
            self._d2 = d2
        else:
            self._d2 = None

    def check_input(self,side):
        if type(side) == type(1.0) or type(side) == type(1):
            return True
        return False

    def area(self):
        return .5 * self._d1 * self._d2

class Parallelogram(Quadrilateral):
    def __init__(s1,s2,s3,s4,b,h):
        super().__init__(s1,s2,s3,s4)
        if self.check_input(b):
            self._b = b
        else:
            self._b = None

        if self.check_input(d2):
            self._h = h
        else:
            self._h = None

    def check_input(self,side):
        if type(side) == type(1.0) or type(side) == type(1):
            return True
        return False

    def area(self):
        return .5 * self._b * self._h

class 
        


        
        
    
