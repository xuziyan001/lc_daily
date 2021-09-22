
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tool import ListNode, concat_node


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        prepre = None
        while pre and cur:
            tmp = cur.next
            cur.next = pre
            pre.next = prepre
            prepre = cur
            pre = tmp
            if pre:
                cur = pre.next
        if pre:
            pre.next = prepre
            return pre
        return prepre

    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre



if __name__ == '__main__':
    l = [1,2]
    ll = concat_node(l)
    t = Solution().reverseList(ll)
    print(t)

