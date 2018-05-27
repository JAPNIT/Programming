class stack():
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None for i in range(capacity)]
        self._top = 0

    def is_full(self):
        if self._top == self._capacity:
            return True
        return False

    def is_empty(self):
        if self._top == 0:
            return True
        else:
            return False
    
    def push(self,val):
        if self.is_full():
            print("Stack full")
        else:
            self._data[self._top] = val
            self._top += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self._data[self._top-1] = None
            self._top -= 1
        # OR
        # self._top -= 1
        # self._data = self._data[:self._top]

    def print(self):
        print (self._data)
        
