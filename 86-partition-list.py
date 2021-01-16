"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。
"""

"""
直观的双链表
"""
from tool import ListNode, concat_node


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        i = head
        i_tail = None
        while True:
            while i and i.val < x:
                i_tail = i
                i = i.next
            if not i:
                return head
            j = i
            j_tail = i_tail
            while j and j.val >= x:
                j_tail = j
                j = j.next
            if not j:
                return head
            # swap i,j
            j_tail.next = j.next
            j.next = i
            if not i_tail:
                head = j
            else:
                i_tail.next = j
            i = j
            i_tail = j


if __name__ == '__main__':
    l = concat_node([1,4,3,2,5,2])
    print(Solution().partition(l, 3))
    print(Solution().partition(l, 4))
    l = concat_node([2,1])
    print(Solution().partition(l, 2))
    l = concat_node([2,1,3])
    print(Solution().partition(l, 2))
