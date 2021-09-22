from tool import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        pre = head
        current = head.next
        while current:
            if current.val == val:
                pre.next = current.next
                current = current.next
            else:
                pre = pre.next
                current = current.next
        return head
