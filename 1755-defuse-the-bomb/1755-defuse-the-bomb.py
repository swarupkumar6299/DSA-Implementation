class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        if k < 0:
            code.reverse()
            k = -k
            reversed_flag = True
        else:
            reversed_flag = False

        pre = [0] * n
        pre[0] = code[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + code[i]

        res = [0] * n
        for i in range(n):
            if i + k < n:
                res[i] = pre[i + k] - pre[i]
            else:
                res[i] = (pre[n - 1] - pre[i]) + pre[(i + k) % n]

        if reversed_flag:
            res.reverse()

        return res