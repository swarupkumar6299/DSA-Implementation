class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        LRG = 1_000_000

        @cache
        def minc(i, j, f):
            if i + 1 >= j:
                return 0
            return minc(i + f, j - f, f) + (s[i] != s[j - 1])
        
        @cache
        def min2sp(i, j):
            n = j - i
            res = LRG
            for d in range(1, floor(n ** 0.5) + 1):
                f, rem = divmod(n, d)
                if rem == 0:
                    res = min(res, sum(minc(i + d0, j + 1 - d + d0, d) for d0 in range(d)))
                    if f != d and f != n:
                        res = min(res, sum(minc(i + f0, j + 1 - f + f0, f) for f0 in range(f)))
            return res
        
        @cache
        def check(i, _k):
            if _k == 0:
                return LRG if i != len(s) else 0
            _k -= 1
            ans = LRG
            for j in range(i + 2, len(s) - 2 * _k + 1):
                ans = min(ans, min2sp(i, j) + check(j, _k))
            return ans
        
        return check(0, k)