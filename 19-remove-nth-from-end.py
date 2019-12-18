from tool import ListNode, concat_node


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针，first先走n步，first到头后second即需要移除的node
        if head is None or head.next is None:
            return None
        first = head
        for i in range(n-1):
            first = first.next
        if first.next is None:
            # remove first
            return head.next
        first = first.next
        second = head
        while first:
            first = first.next
            if first is None:
                # second.next to remove
                second.next = second.next.next
            else:
                second = second.next
        return head


if __name__ == '__main__':
    l = concat_node([1,2,3,4,5])
    print(Solution().removeNthFromEnd(l, 2))
    l = concat_node([1,2,3,4,5])
    print(Solution().removeNthFromEnd(l, 1))
    l = concat_node([1])
    print(Solution().removeNthFromEnd(l, 1))
    l = concat_node([1,2])
    print(Solution().removeNthFromEnd(l, 2)) # 2
