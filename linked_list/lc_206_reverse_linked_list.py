def reverseList(self, head):
    prev, curr = None, head

    while curr:
        nxt = curr.next

        curr.next = prev
        prev = curr