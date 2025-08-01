class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = [[1],[1,1]]
        if numRows==1:
            return li[:1]
        elif numRows==2:
            return li
        l = [1]
        for i in range(2,numRows):
            for j in range(1,len(li[-1])):
                l.append(li[-1][j-1]+li[-1][j])
            l.append(1)
            li.append(l)
            l = [1]
        return li