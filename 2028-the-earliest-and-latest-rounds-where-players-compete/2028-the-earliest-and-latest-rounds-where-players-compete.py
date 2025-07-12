class Solution:
    def __init__(self):
        self.ans=[]
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def solve(arr,r,f,s):
            #print(self.ans,arr)
            if not arr:
                return
            r+=1
            arr.sort()
            ar=[]
            nn=len(arr)
            x,y=[],[]
            for i in range(nn//2):
                if arr[i]==f and arr[nn-i-1]==s:
                    self.ans.append(r)
                    return
                if arr[i]==f or arr[i]==s:
                    ar.append(arr[i])
                    continue
                 
                if arr[nn-i-1]==s or arr[nn-i-1]==f:
                    ar.append(arr[nn-i-1])
                    continue
                else:
                    x.append(arr[i])
                    y.append(arr[nn-i-1])
            if nn%2==1:
                ar.append(arr[nn//2])
            #print(ar,x,y)
            nnnn = len(x)
            resultss = []
            for ii in range(2**nnnn):
                combo = []
                for jj in range(nnnn):
                    # Check j-th bit of i
                    if (ii >> jj) & 1:
                        combo.append(x[jj])
                    else:
                        combo.append(y[jj])
                resultss.append(combo)
            #print(resultss)
            for i in resultss:
                dj=ar.copy()+i
                #print(dj)
                solve(dj,r,f,s)
        a=[i+1 for i in range(n)]
        rounds=0
        solve(a,rounds,firstPlayer,secondPlayer)
        self.ans.sort()
        #print(self.ans)
        return [self.ans[0],self.ans[-1]]