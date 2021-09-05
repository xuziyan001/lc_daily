"""
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

"""
from tool import ListNode, concat_node


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        start = head
        sorted_head = head
        start = start.next
        sorted_head.next = None
        while start:
            new_start = sorted_head
            pre = sorted_head
            while new_start and start.val >= new_start.val:
                pre = new_start
                new_start = new_start.next
            if not new_start: #max
                pre.next = start
                start = start.next
                pre.next.next = None
                continue
            # insertion
            if new_start == sorted_head:
                tmp = start.next
                start.next = sorted_head
                sorted_head = start
                start = tmp
            else:
                tmp = start.next
                pre.next = start
                start.next = new_start
                start = tmp
        return sorted_head


if __name__ == '__main__':
    l = concat_node([-1,5,3,4,0])
    print(Solution().insertionSortList(l))