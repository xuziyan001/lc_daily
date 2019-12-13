from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        current = self
        result = ''
        while current.next is not None:
            result += str(current.val) + ','
            current = current.next
        result += str(current.val)
        return result


def concat_node(l: List) -> ListNode:
    head = ListNode(0)
    current = head
    for num in l:
        node = ListNode(num)
        current.next = node
        current = node
    return head.next
