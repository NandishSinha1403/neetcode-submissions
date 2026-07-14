class MyHashMap:

    def __init__(self):
        self.nl = []

    def get(self, key: int) -> int:
        for i in self.nl:
            if i[0] == key:
                return i[1]
        return -1

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val == -1:
            oyi = [key,value]
            self.nl.append(oyi)
        else:
            oyi = [key,val]
            ind = self.nl.index(oyi)
            self.nl[ind] = [key,value]

        


    def remove(self, key: int) -> None:
        value = self.get(key)
        if value == -1:
            return 
        self.nl.remove([key,value])
  

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)