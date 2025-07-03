class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(cur_comb,idx):
            ans.append(cur_comb)
            for i in range(idx,n):
                dfs([nums[i]]+cur_comb,i+1)
        dfs([],0)
        return ans

        