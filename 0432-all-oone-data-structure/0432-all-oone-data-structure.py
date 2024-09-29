class AllOne:

    def __init__(self):
        self.my_dict = {}
        

    def inc(self, key: str) -> None:
        if key in self.my_dict.keys():
            self.my_dict[key] += 1
        else:
            self.my_dict[key] = 1
        

    def dec(self, key: str) -> None:
        if key in self.my_dict.keys():
            self.my_dict[key] -= 1
            if self.my_dict[key] == 0:
                self.my_dict.pop(key)

    def getMaxKey(self) -> str:
        if not self.my_dict:
            return ""
        res = 0
        maxi = float('-inf')
        for key in self.my_dict.keys():
            if self.my_dict[key] > maxi:
                maxi = self.my_dict[key]
                res = key
        return res


    def getMinKey(self) -> str:
        if not self.my_dict:
            return ""
        res = 0
        mini = float('inf')
        for key in self.my_dict.keys():
            if self.my_dict[key] < mini:
                mini = self.my_dict[key]
                res = key
        return res
        
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()