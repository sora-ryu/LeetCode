class RandomizedSet:

    def __init__(self):
        self.set = {}
        

    def insert(self, val: int) -> bool:
        if not val in self.set:
            self.set[val] = None
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.set:
            del self.set[val]
            return True
        return False
    

    def getRandom(self) -> int:
        return random.choice(list(self.set.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()