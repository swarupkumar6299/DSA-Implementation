class Solution:
    def maxSubsequence(self, nums,k):
        pairs = [(num,i) for i, num in enumerate(nums)] #pair number with index
        pairs.sort(key=lambda x: -x[0]) # sort by number decending
        top_k = pairs[:k] # take top k
        top_k.sort(key=lambda x: x[1]) # Sort by original index
        return [num for num, _ in top_k] # Return only the numbers


        