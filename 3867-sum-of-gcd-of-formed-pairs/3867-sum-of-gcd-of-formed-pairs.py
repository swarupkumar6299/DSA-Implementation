class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx,smGcd, n = 0,0, len(nums) // 2
        for num in nums:
            if num>mx:mx = num
            prefixGcd.append(gcd(num,mx))
        prefixGcd.sort()
        for i in range(n):
            smGcd+= gcd(prefixGcd[i], prefixGcd[~i])
        return smGcd
        