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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def concat_node(l: List) -> ListNode:
    head = ListNode(0)
    current = head
    for num in l:
        node = ListNode(num)
        current.next = node
        current = node
    return head.next


def concat_tree(l: List) -> TreeNode:
    nodes = [TreeNode(x) for x in l]
    n = len(nodes)
    leaves = n // 2
    for i in range(n-leaves):
        left = 2*i+1
        if left < n:
            nodes[i].left = nodes[left]
        right = 2*i+2
        if right < n:
            nodes[i].right = nodes[right]
    return nodes[0]
