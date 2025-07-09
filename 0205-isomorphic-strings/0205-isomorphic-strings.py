class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}  #s-->t
        for i in range(len(s)):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            elif t[i] in m.values():
                return False
            else:
                m[s[i]] = t[i]
        return True