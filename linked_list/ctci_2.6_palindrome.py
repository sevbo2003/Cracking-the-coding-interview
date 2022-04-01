""" 
LeetCode: https://leetcode.com/problems/palindrome-linked-list/

Problem: check is the linked list is palindrome.

Solution:
0. We will use stack, go till middle by pusing, and pop another middle.
1. Use fast and slow pointers. Fast pointer moves 2 steps at a time, slow pointer moves 1 step at a time.
2. While fast reaches the end, the slow will stand in middle. Push to stack.
3. Check for even and odd length of LL. If odd fast will be in last element, so move slow to one.
4. Pop from stack and check the values. Slow ptr is in middle.

Time: O(n)
Space: O(n)
"""

from linked_list import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
           return None
        if head.next is None:
            return True
        
        stack = []
        
        fast, slow = head, head
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        if fast is not None:
            slow = slow.next
            
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
            
        return True
