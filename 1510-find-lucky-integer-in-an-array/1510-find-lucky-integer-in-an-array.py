class Solution:
    def findLucky(self, arr: List[int]) -> int:

        count = Counter(arr)
        res = []
        for key,value in count.items():
            if key == value:
                res.append(key)
        return max(res) if res else -1      