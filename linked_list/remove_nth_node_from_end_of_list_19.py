"""
Given the head of the linked list, I need to delete the nth element.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0. First need to change the n to count from the beginning
        # 1. need to traverse through the LL, with count
        # 2. prev, curr

        curr = head
        count_length = 0

        while curr is not None:
            curr = curr.next
            count_length += 1

        target = count_length - n + 1  # Target index from the beginning

        if target == 1:
            return head.next

        prev_node = head
        curr = head
        count_length = 0

        while curr is not None:
            count_length += 1

            if count_length == target:
                prev_node.next = curr.next
            prev_node = curr
            curr = curr.next

        return head
