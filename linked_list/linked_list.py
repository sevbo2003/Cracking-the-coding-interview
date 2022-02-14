class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    size = 0

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head

        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            # taking the partition till "index"
            for i in range(index - 1):
                curr = curr.next

            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next

            curr.next = curr.next.next
        self.size -= 1


    def __repr__(self):
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append(str(curr.val))
            curr = curr.next

        return "->".join(nodes)

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)
print(obj, obj.size)

param_1 = obj.get(2)

obj.addAtTail(4)
print(obj)

obj.addAtIndex(1, 56)
print(obj)

obj.deleteAtIndex(1)
print(obj)
