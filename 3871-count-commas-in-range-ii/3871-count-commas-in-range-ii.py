class Solution:
    def countCommas(self, n: int) -> int:
        if n < 10**3:
            return 0
        elif n < 10**6:
            return (n - 10**3 + 1) * 1
        elif n < 10**9:
            return 999_000 + (n - 10**6 + 1) * 2
        elif n < 10**12:
            return 1_998_999_000 + (n - 10**9 + 1) * 3
        elif n < 10**15:
            return 2_998_998_999_000 + (n - 10**12 + 1) * 4
        else:
            return 3_998_998_998_999_000 + (n - 10**15 + 1) * 5
        