class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        hills= valleys=0
        prev=nums[0]
        curr=nums[1]
        next1= nums[2]
        while i<len(nums)-1:
            i+=1
            next1=nums[i]
            if prev<curr>next1:
                hills+=1
            elif prev>curr<next1:
                valleys+=1
            prev = prev if curr==next1 else curr
            curr= next1
        return hills+valleys
        