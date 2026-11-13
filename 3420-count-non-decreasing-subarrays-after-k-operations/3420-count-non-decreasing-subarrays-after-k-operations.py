class Solution:
    def countNonDecreasingSubarrays(self, A: List[int], k: int) -> int:
        '''
        [4, 3, 2, 1, 6]
        

        '''
        N = len(A)
        A.reverse()
        l = 0
        q = deque()
        ans = 0

        for r in range(N):
            while q and A[q[-1]] < A[r]:
                ll = q.pop()
                lll = q[-1] if q else l - 1
                amt = ll - lll
                diff = A[r] - A[ll]
                k -= diff * amt

            q.append(r)
            while k < 0:
                diff = A[q[0]] - A[l]
                k += diff
                if l == q[0]:
                    q.popleft()

                l += 1

            


            ans += r - l + 1

        
        return ans