# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from tool import ListNode, concat_node


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        t = head
        count = 0
        tail = head
        while t:
            count += 1
            if not t.next:
                tail = t
            t = t.next
        k = k % count
        if k == 0:
            return head
        new_head = head
        mov = count - k
        new_tail = head
        while mov:
            if mov == 1:
                new_tail = new_head
            new_head = new_head.next
            mov -= 1
        tail.next = head
        new_tail.next = None
        return new_head


if __name__ == '__main__':
    l = concat_node([1,2,3,4,5])
    print(Solution().rotateRight(l, 2))
    l = concat_node([0,1,2])
    print(Solution().rotateRight(l, 4))
