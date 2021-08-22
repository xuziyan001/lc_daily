#
# 给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 返回其自底向上的层序遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii

from typing import List

from tool import TreeNode, concat_tree


class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        def layered(layer_stack):
            layer_list = list()
            next_stack = list()
            for each in layer_stack:
                layer_list.append(each.val)
                if each.left:
                    next_stack.append(each.left)
                if each.right:
                    next_stack.append(each.right)
            result.append(layer_list)
            return next_stack
        stack = [root]
        while stack:
            stack = layered(stack)
        result.reverse()
        return result


if __name__ == '__main__':
    s = concat_tree([3,9,20,None,None,15,7])
    r = Solution().levelOrderBottom(s)
    print(r)