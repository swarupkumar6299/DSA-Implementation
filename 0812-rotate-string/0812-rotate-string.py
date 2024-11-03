class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1 = list(s)
        g1 = list(goal)
        if len(s) != len(goal):
            return False
        else:
            for i in range(len(s)):
                letter = s1.pop(0)
                s1.append(letter)
                if s1 == g1:
                    return True
                    break
            return False