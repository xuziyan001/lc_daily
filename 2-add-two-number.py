# Definition for singly-linked list.

from tool import ListNode, concat_node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        forward = 0
        head = ListNode(0)
        current = head
        while l1 is not None or l2 is not None or forward != 0:
            if l1 is None:
                l1val = 0
            else:
                l1val = l1.val
            if l2 is None:
                l2val = 0
            else:
                l2val = l2.val
            s = l1val + l2val + forward
            forward = 0
            if s >= 10:
                forward = 1
                s -= 10
            node = ListNode(s)
            current.next = node
            current = node
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return head.next


if __name__ == "__main__":
    l1 = concat_node([2,4,3])
    l2 = concat_node([5,6,4])
    print(Solution().addTwoNumbers(l1,l2))
    l1 = concat_node([1,9,9])
    l2 = concat_node([9])
    print(Solution().addTwoNumbers(l1,l2))

