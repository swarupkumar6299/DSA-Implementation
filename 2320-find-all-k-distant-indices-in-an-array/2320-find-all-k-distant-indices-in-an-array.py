class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]==key:
                a.append(i)
        for i in range(len(nums)):
            for j in a:
                if abs(i-j)>k:
                    continue
                else:
                    res.append(i)
        return list(set(res))
                
        

        


        