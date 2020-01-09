from tool import ListNode, concat_node


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        b = None
        b_tail = None
        c = head
        last_dup = -pow(2,31)
        while c:
            if c.next:
                # remove
                if c.val == c.next.val:
                    last_dup = c.val
                    c = c.next
                else:
                    if c.val == last_dup:
                        c = c.next
                        continue
                    if not b:
                        b = c
                        b_tail = c
                        c = c.next
                        b_tail.next = None
                    else:
                        b_tail.next = c
                        b_tail = c
                        c = c.next
                        b_tail.next = None
                    # append
            else:
                if c.val == last_dup:
                    c = c.next
                    continue
                if not b:
                    b = c
                else:
                    b_tail.next = c
                c = c.next
        return b


if __name__ == '__main__':
    l = concat_node([1,1,2])
    print(Solution().deleteDuplicates(l))
    l = concat_node([1,1,2,3,3])
    print(Solution().deleteDuplicates(l))
    l = concat_node([2,1])
    print(Solution().deleteDuplicates(l))

