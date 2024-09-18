# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Initialize odd and even pointers
        odd = head
        even = head.next
        evenStart = head.next
        
        # Traverse the list, re-linking odd and even nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        # Connect the end of odd-indexed nodes to the start of even-indexed nodes
        odd.next = evenStart
        
        return head
