class Solution:
  def maxSelectedElements(self, nums: list[int]) -> int:
    ans = 0
    # {num: the length of the longest consecutive elements ending in num}
    dp = {}
    nums.sort()

    for num in nums:
        dp[num + 1] = dp.get(num, 0) + 1
        dp[num] = dp.get(num - 1, 0) + 1
        ans = max(ans, dp[num + 1], dp[num])

    return ans