from tool import ListNode, concat_node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        i = head
        while l1 and l2:
            if l1.val > l2.val:
                node = ListNode(l2.val)
                l2 = l2.next
            else:
                node = ListNode(l1.val)
                l1 = l1.next
            i.next = node
            i = i.next
        if l1 is None:
            i.next = l2
        if l2 is None:
            i.next = l1
        return head.next


if __name__ == '__main__':
    l1 = concat_node([1,2,3])
    l2 = concat_node([2,3,4])
    print(Solution().mergeTwoLists(l1,l2))
