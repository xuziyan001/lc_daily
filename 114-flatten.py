#
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
#展开后的单链表应该与二叉树 先序遍历 顺序相同。

from tool import concat_tree, TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        l = []
        def preOrder(root):
            l.append(root)
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)
        preOrder(root)
        current = root
        for i in l[1:]:
            current.right = i
            current.left = None
            current = current.right


if __name__ == '__main__':
    r = [1,2,5,3,4,None,6]
    t = concat_tree(r)
    Solution().flatten(t)
    print(t)

