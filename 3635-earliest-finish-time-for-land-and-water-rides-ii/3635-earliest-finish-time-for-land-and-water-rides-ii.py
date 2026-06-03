class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        def f(a,b,aa,bb):
            e = min(map(add,a,b))
            return min(max(s,e)+d for s,d in zip(aa,bb))
        return min(f(ls,ld,ws,wd),f(ws,wd,ls,ld))
        