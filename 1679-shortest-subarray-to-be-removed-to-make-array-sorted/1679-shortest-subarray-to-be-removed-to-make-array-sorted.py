class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        n = len(arr)
        left = 0
        right = n - 1
        
        # Find longest non-decreasing prefix
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        
        # If already sorted
        if left == n - 1:
            return 0
        
        # Find longest non-decreasing suffix
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Minimum length considering removing prefix or suffix
        shortest_subarray_length = min(n - left - 1, right)
        
        # Try merging prefix and suffix to find a better result
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                shortest_subarray_length = min(shortest_subarray_length, j - i - 1)
                i += 1
            else:
                j += 1
        
        return shortest_subarray_length