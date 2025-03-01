class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        i = -1
        for j in range(len(nums)):
            if nums[j]!=0:
                i+=1
                nums[i], nums[j]= nums[j], nums[i]
        return nums