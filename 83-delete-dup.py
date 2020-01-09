from tool import ListNode, concat_node


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        current = head.val
        b = head
        c = head.next
        b.next = None
        tail = b
        while c:
            if c.val == current:
                # remove
                c = c.next
            else:
                tmp = c
                c = c.next
                tmp.next = None
                tail.next = tmp
                tail = tmp
                current = tmp.val
        return b


if __name__ == '__main__':
    l = concat_node([1,1,2])
    print(Solution().deleteDuplicates(l))
    l = concat_node([1,1,2,3,3])
    print(Solution().deleteDuplicates(l))

