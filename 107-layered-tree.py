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
        stack = []
        stack.append(root)
        layer = 0
        while stack:
            r = stack[0]
            result.append(r)
            if r:
                stack.append(r.left)
                stack.append(r.right)
            else:
                stack.extend([None, None])





    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        tmp = [root]
        while len([x for x in tmp if x is not None]) != 0:
            result.append([x.val for x in tmp if x is not None])
            next_level = []
            for each in tmp:
                if each:
                    next_level.append(each.left)
                    next_level.append(each.right)
                else:
                    next_level.append(None)
                    next_level.append(None)
            tmp = next_level
        result.reverse()
        return result


if __name__ == '__main__':
    s = concat_tree([3,9,20,None,None,15,7])
    r = Solution().levelOrderBottom(s)
    print(r)