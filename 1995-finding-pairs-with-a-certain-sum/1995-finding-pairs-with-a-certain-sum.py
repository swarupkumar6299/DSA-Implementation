class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.cnt2[old]-=1
        new = old+val
        self.nums2[index]=new
        self.cnt2[new]+=1
    def count(self, tot: int) -> int:
        cnt = 0
        for x in self.nums1:
            cnt+=self.cnt2.get(tot - x,0)
        return cnt


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)