class MyHashMap:

    def __init__(self):
        self.values = []
        self.keys = []
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        self.values[self.keys.index(key)] = value

        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1 

        return self.values[self.keys.index(key)]
        

    def remove(self, key: int) -> None:
        if key not in self.keys:
            return 

        nr = self.keys.index(key)
        self.keys.remove(key)
        del self.values[nr]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)