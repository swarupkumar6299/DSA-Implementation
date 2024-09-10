class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        # Move non-zero elements to the front
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        # Set the remaining elements to 0
        while i < len(nums):
            nums[i] = 0
            i += 1
