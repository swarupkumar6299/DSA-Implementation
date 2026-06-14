# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        value = []
        current = head
        while current:
            value.append(current.val)
            current = current.next
        max_sum = 0
        n = len(value)
        for i in range(n//2):
            twin_sum = value[i] + value [n-1-i]
            max_sum = max(max_sum,twin_sum)
        return max_sum