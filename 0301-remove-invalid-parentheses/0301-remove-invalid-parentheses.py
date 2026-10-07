from itertools import product

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        groups = []
        group = ['', s[0]]
        for i in range(1, n):
            if s[i] in '()':
                if group[-1][-1] == s[i]:
                    group.append(group[-1] + s[i])
                else:
                    groups.append(group)
                    group = ['', s[i]]
            else:
                if group[-1][-1] not in '()':
                    group[-1] = group[-1] + s[i]
                else:
                    groups.append(group)
                    group = ['', s[i]]
        groups.append(group)

        ans = set()
        longest = 0
        for p in product(*groups):
            t = ''.join(p)
            if len(t) < longest:
                continue
            cur = 0
            for c in t:
                if c == '(':
                    cur += 1
                elif c == ')':
                    cur -= 1
                    if cur < 0:
                        break
            if cur != 0:
                continue
            if len(t) > longest:
                longest = len(t)
                ans = {t}
            else:
                assert len(t) == longest
                ans.add(t)
        return list(ans)