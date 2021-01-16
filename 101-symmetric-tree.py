"""
给定一个二叉树，检查它是否是镜像对称的。

"""
"""
递归的思路
"""
from tool import TreeNode, concat_tree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSem(root.left, root.right)

    def isSem(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.isSem(left.left, right.right) and self.isSem(left.right, right.left)


if __name__ == '__main__':
    t = concat_tree([1,2,2,3,4,4,3])
    s = Solution()
    print(s.isSymmetric(t))
