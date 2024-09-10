# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1,head)
        current = new_head

        while current.next is not None and current.next.next is not None:
        #We always want to operate on current.next
            v1 = current.next.val
            v2 = current.next.next.val

            g = math.gcd(v1,v2) 
            new_node = ListNode(g)
            next_node = current.next.next
            current.next.next = new_node
            new_node. next = next_node
            current = current.next.next
        return new_head.next
        