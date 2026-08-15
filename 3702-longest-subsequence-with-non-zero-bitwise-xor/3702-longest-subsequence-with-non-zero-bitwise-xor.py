 # class Solution:
#     def longestSubsequence(self, nums: List[int]) -> int:
#         total_xor = 0
#         has_nonzero = False
#         for num in nums:
#             total_xor ^= num
#             if total_xor !=0:
#                 has_nonzero = True

#         if not has_nonzero:
#             return 0

#         if total_xor != 0:
#             return len(nums)

#         return len(nums) - 1
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        if [0]*(n)==nums:
            return 0
        x=0
        for i in nums:
            x^=i
        return n if x else n-1
        
        