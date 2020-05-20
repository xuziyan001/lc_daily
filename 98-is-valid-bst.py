"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
"""
这里的思路比较简单，首先递归判断给定的条件
递归过程中需要满足左子树中所有的值都小于当前节点，即左子树最右节点需要小于当前节点
右子树同理
"""

from tool import TreeNode, concat_tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = root.left
        right = root.right
        if left:
            if left.val >= root.val:
                return False
        if right:
            if right.val <= root.val:
                return False
        if not (self.isValidBST(left) and self.isValidBST(right)):
            return False
        # 找到左子树最大值与右子树最小值
        left_max = root.val-1
        while left:
            left_max = left.val
            left = left.right
        right_min = root.val+1
        while right:
            right_min = right.val
            right = right.left
        return (root.val > left_max) and (root.val < right_min)


if __name__ == '__main__':
    l = concat_tree([5,1,4,None,None,3,6])
    print(l)
    print(Solution().isValidBST(l))
    l = concat_tree([2,1,3])
    print(Solution().isValidBST(l))
    l = concat_tree([10,5,15,None,None,6,20])
    print(l)
    print(Solution().isValidBST(l))
