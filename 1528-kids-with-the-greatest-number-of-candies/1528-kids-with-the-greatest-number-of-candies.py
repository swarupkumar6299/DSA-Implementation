class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result_lst = []
        max_num = max(candies)
        for num in candies:
            result_lst.append(num+extraCandies >= max_num)
        return result_lst