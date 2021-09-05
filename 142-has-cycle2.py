
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

"""
from tool import ListNode, concat_node, get_node


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        renew = head
        slow = slow.next
        while renew != slow:
            renew = renew.next
            slow = slow.next
        return renew


if __name__ == '__main__':
    l = concat_node([3,2,0,-4])
    get_node(l, 3).next = get_node(l, 1)
    print(Solution().detectCycle(l))
