import bisect
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if nums == sorted(nums) and len(set(nums)) == len(nums):
            return True
        def sieve_of_eratosthenes(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0], is_prime[1] = False, False  
            for num in range(2, int(limit ** 0.5) + 1):
                if is_prime[num]:
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
            primes = [num for num in range(2, limit + 1) if is_prime[num]]
            return primes
        arr = sieve_of_eratosthenes(1000)
        for i in range(len(nums)):
            if i == 0:
                ind = bisect.bisect_left(arr,nums[i])
                if ind == 0:
                    continue
                nums[i] -= arr[ind-1]
            else:
                if nums[i] <= nums[i-1]:
                    return False
                val = nums[i] - nums[i-1]
                ind = bisect.bisect_left(arr,val)
                if ind == 0:
                    continue
                nums[i] -= arr[ind-1]
        if nums == sorted(nums):
            return True
        return False






        