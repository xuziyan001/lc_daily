from tool import ListNode, concat_node
"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。
"""


class Solution:

    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        # 需要开始反转的head
        head = pre.next
        # 开始翻转，本质上是把后续所有节点插入到pre与head之间
        for i in range(m, n):
            second = head.next
            head.next = second.next
            second.next = pre.next
            pre.next = second
        return dummy.next

    def reverseBetween2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            if n == 1:
                return
            right = right.next
            if m > 1:
                left = left.next
            # 以迭代替代prev指针
            recurseAndReverse(right, m - 1, n - 1)
            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next
        recurseAndReverse(right, m, n)
        return head


if __name__ == '__main__':
    l = concat_node([1,2,3,4,5,6])
    print(Solution().reverseBetween(l, 2, 4))
    l = concat_node([1,2,3,4,5,6])
    print(Solution().reverseBetween2(l, 2, 4))
