# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]
        pos = 0
        prev = head
        cur = head.next
        nxt = head.next.next
        firstDisctinct = -1
        lastDisctinct = -1
        minDistance = float("inf")
        while nxt:
            if (cur.val > prev.val and cur.val > nxt.val) or (
                cur.val < prev.val and cur.val < nxt.val
            ):
                if firstDisctinct == -1:
                    firstDisctinct = pos
                else:
                    minDistance = min(minDistance, pos - lastDisctinct)
                lastDisctinct = pos
            prev = prev.next
            cur = cur.next
            nxt = nxt.next
            pos += 1
        if firstDisctinct == -1 or lastDisctinct == firstDisctinct:
            return [-1, -1]
        return [minDistance, lastDisctinct - firstDisctinct]