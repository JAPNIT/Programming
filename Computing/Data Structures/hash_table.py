class HashTable():
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None for i in range(capacity)]

    def hash(self, str_val):
        val = 0
        for i in range(len(str_val)):
            val += (i+1) * ord(str_val[i])
        return val % self._capacity

    def insert(self,str_val):
        key = self.hash(str_val)
        if self._data[key] == None:
            self._data[key] = str_val
            return 1
        else:
            for i in range(self._capacity):
                current_index = (key+1) % self._capacity
                key += 1
                if self._data[current_index] == None:
                    self._data[current_index] = str_val
                    return 1
        print("Couldn't insert")
                

    def print(self):
        print(self._data)

    def delete(self,str_val):
        key = self.hash(str_val)
        if self._data[key] == str_val:
            self._data[key] = None
            return 1
        else:
            for i in range(self._capacity):
                current_index = (key+1) % self._capacity
                key += 1
                if self._data[current_index] == str_val:
                    self._data[current_index] = None
                    return 1
        print("Couldn't delete")
            
