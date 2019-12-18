from typing import List

from tool import ListNode, concat_node


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = [node for node in lists if node is not None]
        head = ListNode(0)
        current = head
        while k:
            next_val = self.get_next(k)
            node = ListNode(next_val)
            current.next = node
            current = node
            k = list(filter(lambda x: x is not None, k))
        return head.next

    def get_next(self, k):
        min_index = 0
        for i in range(1, len(k)):
            if k[i].val < k[min_index].val:
                min_index = i
        min_val = k[min_index].val
        k[min_index] = k[min_index].next
        return min_val

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        k = [node for node in lists if node is not None]
        k.sort(key=lambda x: x.val)
        head = ListNode(0)
        current = head
        while k:
            node = ListNode(k[0].val)
            k[0] = k[0].next
            current.next = node
            current = node
            if k[0] is None:
                k = k[1:]
                continue
            if len(k) == 1:
                continue
            if k[1].val >= k[0].val:
                continue
            # k[0] is the max
            if k[-1].val <= k[0].val:
                k = k[1:] + [k[0]]
                continue
            # sort k
            for i in range(1, len(k)):
                if k[i].val > k[0].val:
                    k = k[1:i] + [k[0]] + k[i:]
                    break
        return head.next


if __name__ == '__main__':
    l1 = concat_node([1,2,3])
    l2 = concat_node([1,2,3])
    l3 = concat_node([2,2,3])
    l = [l1,l2,l3]
    print(Solution().mergeKLists2(l))
    l = [concat_node([1, 4, 5]), concat_node([1, 3, 4]), concat_node([2, 6])]
    print(Solution().mergeKLists2(l))
    l = [concat_node([])]
    print(Solution().mergeKLists2(l))
