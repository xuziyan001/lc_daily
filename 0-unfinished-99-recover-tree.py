from tool import TreeNode, concat_tree

"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。
"""

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 直接中序遍历再将排序好的节点填回去即可获得O(n)空间的算法
        # 下面我们实现Morris Traversal方法
        cur = root
        node1, node2 = None, None
        pre = None
        while cur:
            # cur左子树为空，输出当前节点并指向右节点
            if cur.left is None:
                if pre is not None and pre.val > cur.val:
                    node1 = pre if node1 is None else node1
                    node2 = cur
                pre = cur
                cur = cur.right
            else:
                pre = cur.left
                while (pre.right is not None) and (pre.right != cur):
                    pre = pre.right
                # pre为当前cur所属的前驱节点, 此时pre指向当前节点，cur左移
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                # pre的右节点为cur，需要将pre的右节点重新置空，并输出当前节点，cur右移
                else:
                    pre.right = None
                    if pre is not None and pre.val > cur.val:
                        node1 = pre if node1 is None else node1
                        node2 = cur
                    pre = cur
                    cur = cur.right
        node1.val, node2.val = node2.val, node1.val

    def morris_in_order(self, root):
        cur = root
        res = []
        while cur:
            # cur左子树为空，输出当前节点并指向右节点
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while (pre.right is not None) & (pre.right != cur):
                    pre = pre.right
                # pre为当前cur所属的前驱节点, 此时pre指向当前节点，cur左移
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                # pre的右节点为cur，需要将pre的右节点重新置空，并输出当前节点，cur右移
                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res


if __name__ == '__main__':
    l = [1,3,None,None,2]
    t = concat_tree(l)
    print(t)
    print(Solution().recoverTree(t))
    print(t)

    l = [3,1,4,None,None,2]
    t = concat_tree(l)
    print(t)
    print(Solution().recoverTree(t))
    print(t)
