class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        for pair in knowledge:
            d[pair[0]] = pair[1]
        bracket = False
        res = ""
        for char in s:
            if char == '(':
                bracket = True
                temp = ""
                continue
            elif char == ')':
                if temp in d:
                    res += d[temp]
                else:
                    res += '?'
                bracket = False
                continue
            if bracket:
                temp += char
            else:
                res += char
        return res
        