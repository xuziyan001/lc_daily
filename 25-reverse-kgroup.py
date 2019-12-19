from tool import ListNode,concat_node


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        if not head:
            return head
        start = head
        end = head
        for i in range(k-1):
            end = end.next
            if not end:
                return head
        new_head = end
        tail = end.next
        # reverse fist
        self.reverse(start, end)
        start.next = tail
        # reverse tails
        prev = start
        start = tail
        end = start
        while end:
            for i in range(k-1):
                end = end.next
                if not end:
                    return new_head
            tail = end.next
            self.reverse(start, end)
            start.next = tail
            prev.next = end
            #
            prev = start
            start = tail
            end = start
        return new_head

    def reverse(self, start, end: ListNode):
        pre = start
        cur = start.next
        nex = cur.next
        tail = end.next
        start.next = None
        # swap first
        cur.next = pre
        while nex != tail:
            pre = cur
            cur = nex
            nex = cur.next
            cur.next = pre


if __name__ == '__main__':
    l = concat_node([1,2,3,4,5])
    print(Solution().reverseKGroup(l, 1))
    l = concat_node([1,2,3,4,5])
    print(Solution().reverseKGroup(l, 2))
    l = concat_node([1,2,3,4,5])
    print(Solution().reverseKGroup(l, 3))
