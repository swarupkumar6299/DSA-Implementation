class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 0
        streak = 0
        current=" "
        for ch in word:
            if ch == current:
                streak+=1
                total+=1
            else:
                current=ch
                streak=1
        return total+1
        