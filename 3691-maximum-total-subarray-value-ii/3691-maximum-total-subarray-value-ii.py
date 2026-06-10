class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        

        tree = [(inf, -inf)] * (len(nums) * 4)


        def build(node, l, r):

            if l == r:
                tree[node] = (nums[l], nums[l])
                return tree[node]

            
            mid = (l + r) // 2

            lmn, lmx = build(node * 2, l, mid)
            rmn, rmx = build(node * 2 + 1, mid + 1, r)

            tree[node] = (min(lmn, rmn), max(lmx, rmx))

            return tree[node]



        def query(node, l, r, l1, r1):

            if l == l1 and r == r1:
                return tree[node]
            
            mid = (l + r) // 2

            mn, mx = inf, -inf
            if l1 <= mid:
                mnn, mxx = query(node * 2, l, mid, max(l, l1), min(mid, r1))
                mn = mnn
                mx = mxx

            if r1 >= mid + 1:
                mnn, mxx = query(node * 2 + 1, mid + 1, r, max(mid + 1, l1), min(r, r1))
                mn = min(mn, mnn)
                mx = max(mx, mxx)
            

            return ((mn, mx))



        build(1, 0, len(nums) - 1)

        # print(tree)

        heap = []
        d = 0
        mx = -inf
        mn = inf
        for i in range(len(nums) - 1, -1, -1):
            mn = min(mn, nums[i])
            mx = max(mx, nums[i])
            heapq.heappush(heap, (-(mx - mn), i, len(nums) - 1))
        
        # print(heap)

        sm = 0
        while k != 0:
            
            d, l, r = heapq.heappop(heap)

            sm += (-d)

            r -= 1 
            if l <= r:
                mn, mx = query(1, 0, len(nums) - 1, l, r)
                heapq.heappush(heap, (-(mx - mn), l, r))

            k -= 1

        
        return (sm)