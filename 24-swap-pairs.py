from tool import ListNode, concat_node


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        first.next = second.next
        second.next = first
        head = second
        # swap tails
        prev = first
        first = first.next
        while first is not None:
            second = first.next
            if second is None:
                break
            tail = second.next
            prev.next = second
            second.next = first
            first.next = tail
            # reset
            prev = first
            first = tail
        return head


if __name__ == '__main__':
    l = concat_node([1,2,3,4])
    print(Solution().swapPairs(l))
