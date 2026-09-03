class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = min([i for i in nums1 if i % 2 == 1], default=-1)
        if min_odd == -1:
            return True
        else:
            min_even = min([i for i in nums1 if i % 2 == 0], default=-1)
            if min_even ==-1:
                return True
            else:
                if min_even - min_odd <1:
                    return False
                else:
                    return True
        