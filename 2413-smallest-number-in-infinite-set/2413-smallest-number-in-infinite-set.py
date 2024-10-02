from sortedcontainers import SortedList
class SmallestInfiniteSet:

    def __init__(self):
        self.seen = [False]*1005

    def popSmallest(self) -> int:
        for i in range (1, 1005):
            if not self. seen [i]:
                self.seen[i] = True
                return i
    def addBack(self, num: int) -> None:
        if num < len(self.seen):
            self.seen[num] = False
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)