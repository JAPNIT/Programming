class queue():
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None for i in range(capacity)]
        self._head = 0
        self._tail = 0

    def is_empty(self):
        if self._tail == self._head and self._data[self._head] == None:
            return True
        return False

    def is_full(self):
        if self._head == self._capacity and self._data[self._head] != None:
            return True
        return False

    def enque(self,val):
        if self.is_full():
            print("Queue is full")
        else:
            self._data[self._tail] = val
            self._tail += 1
        if self._tail >= self._capacity:
            self._tail = 0
            
    def deque(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self._data[self._head] = None
            self._head -= 1

    def print(self):
        print (self._data)
