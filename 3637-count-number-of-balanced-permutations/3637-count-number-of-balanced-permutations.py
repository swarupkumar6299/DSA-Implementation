class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        num = [int(digit) for digit in num]
        self.counter = Counter(num)
        target = sum(num)
        if target % 2 != 0:
            return 0
        target //= 2
        capacity = len(num) // 2
        capacity2 = (len(num) + 1) // 2


        @cache
        def choose(n, k, mod): 
            if k == 0:
                return 1
            if n == 0:
                return 1
            if n == k:
                return 1
            else:
                return (choose(n-1, k-1, mod) + choose(n-1, k, mod)) % mod

        #capacity is how many spots I have left for my even indices
        #capacity2 is how many spots I have left for my odd indices
        @cache
        def permutationsOf(num, target, capacity, capacity2):
            mod = 10 ** 9 + 7
            #some of these might be redundant idk
            if target == 0 and capacity == 0 and capacity2 == 0:
                return 1
            if target < 0:
                return 0
            if target > 0 and capacity == 0:
                return 0
            if target > 0 and num > 9:
                return 0
            if capacity < 0 or capacity2 < 0:
                return 0
            ans = 0
            countNum = self.counter.get(num, 0)
            #try picking 0 0's, 1 0's, 2 0's, 3 0's, etc.
            for pick in range(min(capacity + 1, countNum + 1)):
                unpicked = countNum - pick
                #how many permutations for the rest of the digits?
                partialPermutations = permutationsOf(num + 1, target - (pick * num), capacity - pick, capacity2 - unpicked)
                
                #for each of those permutations, how many ways are there to insert my digits into the even indices?
                insertionWays = choose(capacity, pick, mod)

                #also how many ways are there to insert my other digits into the odd indices?
                otherInsertionWays = choose(capacity2, unpicked, mod)
                newWays = (partialPermutations * insertionWays * otherInsertionWays)
                ans += newWays
                ans %= mod
            return ans % mod

        return permutationsOf(0, target, capacity, capacity2)
                