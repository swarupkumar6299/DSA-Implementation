class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = []
        count = 0
        res = []
        for i in range(k):
            if blocks[i]=="W": 
                count+=1
            l.append(blocks[i])
        mini = count
        for i in range(k,len(blocks)):

            if blocks[i-k]=="W":
                count-=1
            if blocks[i]=="W":
                count+=1

            mini = min(count,mini)
        return mini
      