class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_count = sum(1 for sublist in matrix for num in sublist if num <0)
        total_sum = [abs(num) for sublist in matrix for num in sublist]
        if negative_count % 2==0:
            return sum(total_sum)
        else:
            return sum(total_sum) - 2*min(total_sum)        