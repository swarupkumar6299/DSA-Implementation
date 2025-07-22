class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        curSum = maxSum = 0
        windowVals = set()
        for rightVal in nums:
            while rightVal in windowVals:
                # Move left forward until window is valid
                leftVal = nums[left]
                windowVals.remove(leftVal)
                curSum -= leftVal
                left += 1
                
            # Add the new unique value in
            windowVals.add(rightVal)
            curSum += rightVal
            maxSum = max(curSum, maxSum)
    
        return maxSum