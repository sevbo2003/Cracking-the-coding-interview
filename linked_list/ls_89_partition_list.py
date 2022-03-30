"""
86. Partition List


"""

from linked_list import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
    
        if head.next is None:
            return head
        
        left = ListNode(0)
        dummy_left = left
        
        right = ListNode(0)
        dummy_right = right  
        
        curr = head
        while curr is not None:
            tmp = ListNode(curr.val)
            if tmp.val < x:
                left.next = tmp
                left = left.next
            else:
                right.next = tmp
                right = right.next
            
            curr = curr.next
            
        print(dummy_left.next, "\n", dummy_right.next)
        
        # Concatenate two lists
        left.next = dummy_right.next
        return dummy_left.next
        