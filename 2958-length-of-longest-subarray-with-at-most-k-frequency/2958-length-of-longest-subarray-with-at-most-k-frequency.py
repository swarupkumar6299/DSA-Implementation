class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        count = {}

        for right in range(len(nums)):
            # добавляем правый элемент в окно
            count[nums[right]] = count.get(nums[right], 0) + 1

            # если частота превысила k, сужаем окно слева
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            # обновляем ответ
            ans = max(ans, right - left + 1)

        return ans
        