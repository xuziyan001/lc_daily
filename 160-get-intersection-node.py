"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

题目数据 保证 整个链式结构中不存在环。

"""
from tool import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a and b:
            a = a.next
            b = b.next
        remain = a if a else b
        longer = headA if a else b
        shorter = headA if longer == headB else headB
        counter = 0
        while remain:
            remain = remain.next
            counter += 1
        while counter != 0:
            longer = longer.next
            counter -= 1
        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        return None

