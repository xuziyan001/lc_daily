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

    def __str__(self):
        i = [self]
        result = [self.val]
        while i:
            node = i.pop(0)
            if node.left:
                result.append(node.left.val)
                i.append(node.left)
            else:
                result.append(None)
            if node.right:
                result.append(node.right.val)
                i.append(node.right)
            else:
                result.append(None)
        i = len(result)
        # remove tailed None
        while result[i-1] is None:
            i -= 1
        return str(result[:i])


def concat_node(l: List) -> ListNode:
    head = ListNode(0)
    current = head
    for num in l:
        node = ListNode(num)
        current.next = node
        current = node
    return head.next


def concat_tree(l: List) -> TreeNode:
    nodes = [TreeNode(x) if x is not None else x for x in l]
    n = len(nodes)
    for i in range(n // 2):
        if not nodes[i]:
            continue
        left = 2*i+1
        if left < n:
            nodes[i].left = nodes[left]
        right = 2*i+2
        if right < n:
            nodes[i].right = nodes[right]
    return nodes[0]
