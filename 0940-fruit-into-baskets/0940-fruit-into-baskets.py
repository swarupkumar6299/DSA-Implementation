class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r, res = 0, 0
        basket = collections.defaultdict(int)
        for l in range(len(fruits)):
            basket[fruits[l]] += 1
            while 3 <= len(basket):
                if basket[fruits[r]] == 1:
                    del basket[fruits[r]]
                else:
                    basket[fruits[r]] -= 1
                r += 1
            res = max(res, l - r + 1)

        return res