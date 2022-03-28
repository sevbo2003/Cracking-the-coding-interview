"""
Problem: remove dups in linked list.

Solution: 
1. We can use a hash table to keep track of the elements we've seen so far.

Time: O(n)
Space: O(k), where k is distinc elements in the list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_dups(head):
    """Remove duplicates from a linked list."""
    previous = head
    dupes = {previous.val}
    print(dupes)
    
    while previous.next:
        if previous.next.val in dupes:
            previous.next = previous.next.next
        else:
            dupes.add(previous.next.val)
            previous = previous.next

    return head
