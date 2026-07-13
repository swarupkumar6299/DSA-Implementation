nums = [
    int(num) for d in range(2,10)
    for num in ["123456789"[i: i+d] for i in range(10-d)]
]

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [nums[i] for i in range(bisect_left(nums,low),bisect_right(nums,high))]
        