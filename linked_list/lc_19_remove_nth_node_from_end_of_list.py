"""
19. Remove Nth Node From End of List

Problem: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Solution:
1. Go till the fast n times
2. Check if fast is None return head.next, it happens when fast is the last element, or the only element
3. Then check till fast.next goes to the end
4. Delete the node with slow.next = slow.next.next

General idea, placing the fast to N, then starting iterating.

Time: O(n)
Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next                
        return head
