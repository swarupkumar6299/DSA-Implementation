class Solution:
    def kthSmallestProduct(self, nums1: List[int], num2: List[int], k: int) -> int:
        n2 = len(num2)
        def get_smaller_product(target):
            smaller =0
            for x in nums1:
                if x<0:
                    smaller+=n2-bisect.bisect_left(num2,ceil(target)/x)
                elif x==0:
                    if target>=0:
                        smaller+=n2
                else:
                    smaller+=bisect.bisect_right(num2,target//x)
            return smaller
        def good(target):
            return get_smaller_product(target)>=k
        left=-10**10
        right= 10**10
        while left<right:
            mid=(left+right)//2
            if good(mid):
                right=mid
            else:
                left=mid+1
        return left
            