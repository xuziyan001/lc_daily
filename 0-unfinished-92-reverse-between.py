from tool import ListNode, concat_node
"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。
"""


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        i = head
        i_pre = None
        j = head
        j_aft = None
        for t in range(m-1):
            i_pre = i
            i = i.next
        for t in range(n-1):
            j = j.next
        j_aft = j.next
