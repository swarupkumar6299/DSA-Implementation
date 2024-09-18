# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head . next == None):
            return None
        prevSlow = None
        slow     = head
        fast     = head
        while(fast != None and fast . next != None):
            prevSlow = slow
            slow = slow . next
            fast = fast. next . next
        prevSlow . next = slow . next
        if prevSlow:
            prevSlow.next = slow.next
        
        # Return the modified head
        return head
        