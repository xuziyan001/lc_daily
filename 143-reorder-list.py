"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

 L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换

"""
from tool import ListNode, concat_node


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.findMid(head)
        right_head = mid.next
        # mid = left.tail
        mid.next = None
        new_right = self.reverse(right_head)
        return self.merge(head, new_right)

    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = head
        ne = head.next
        pre.next = None
        while ne:
            tmp = ne.next
            ne.next = pre
            pre = ne
            ne = tmp
        return pre

    def merge(self, left, right):
        l = left
        r = right
        while l and r:
            nl = l.next
            nr = r.next
            l.next = r
            if nl:
                r.next = nl
            l = nl
            r = nr
        return left


if __name__ == '__main__':
    l = concat_node([1,2])
    print(Solution().reorderList(l))
