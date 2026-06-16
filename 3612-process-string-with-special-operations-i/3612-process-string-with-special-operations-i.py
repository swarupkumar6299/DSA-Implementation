class Solution:
    def processStr(self, s: str) -> str:
        current = []
        for c in s:
            if c== "*":
                if len(current)>0:
                    current.pop()
            elif c== "#":
                current = current+current
            elif c=='%':
                current.reverse()
            else:
                current.append(c)
        return "".join(current)
        