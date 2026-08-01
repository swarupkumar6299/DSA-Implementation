class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)

        def dp(i, j, memo):
            if i > j:
                return 0

            if (i, j) not in memo:
                memo[(i, j)] = max(
                    nums[i] - dp(i+1, j, memo),
                    nums[j] - dp(i, j-1, memo)
                )
            return memo[(i, j)]
        return dp(0, n-1, {}) >= 0