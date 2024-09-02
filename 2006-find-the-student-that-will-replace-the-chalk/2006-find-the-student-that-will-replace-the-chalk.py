class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k, i = k% sum (chalk),0
        while k > 0:
            k -= chalk[i]
            if k < 0: return i
            i +=1
        return i
        