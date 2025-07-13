class Solution:
    def isPowerOfTwo(self, nums: int) -> bool:
        i = 0
        while 2**i<=nums:
            if 2**i==nums:
                return True
            i+=1
        return False

        