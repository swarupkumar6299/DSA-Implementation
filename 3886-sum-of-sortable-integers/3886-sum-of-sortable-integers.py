class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        """
        if we want to find the divisors for 36, we check 
        is 36 % 1 = 0 => (1 * 36)
        is 36 % 2 = 0 => (2 * 18)
        is 36 % 3 = 0 => (3 * 12)
        is 36 % 4 = 0 => (4 * 9)
        is 36 % 5 != 0 => NA
        is 36 % 6 = 0 => (6 * 6)
        ...

        now if we check closely, even the reverse will also divide 36, meaning, 

        (36 * 1), (18 * 2), (12 * 3), (4 * 9).

        So every single divisor greater than $\sqrt{36}$ (which is 6) is just the mirror image of a divisor you already found below 6.
        """

        def getDivisors(n):
            divisors = []

            for i in range(1, math.isqrt(n) + 1):
                if n % i == 0:
                    divisors.append(i)
                    
                    if i != n // i: # for > 6 breakpoint from above example
                        divisors.append(n // i)
            
            return divisors
        
        n = len(nums)
        res = 0
        for div in getDivisors(n):
            isDivSortable = True
            i = 0
            prevMax = float("-inf")
            while i < n:
                partition = nums[i: i + div]
                sortedPartition = sorted(partition
                )
                if prevMax > sortedPartition[0]:
                    isDivSortable = False
                    break

                drops = 0
                for j in range(div):
                    if partition[j] > partition[(j + 1) % div]:
                        drops += 1
                
                if drops > 1:
                    isDivSortable = False
                    break
                
                prevMax = sortedPartition[-1]
                i += div

            if isDivSortable:
                res += div
        
        return res
