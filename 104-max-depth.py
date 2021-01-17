"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
"""
from typing import List

from tool import TreeNode, concat_tree


class Solution:

    def __init__(self):
        self.deepth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.bfs([root])
        return self.deepth

    def bfs(self, current_list: List[TreeNode]):
        if len(current_list) == 0:
            return
        # 到达下一层
        result = []
        leveled_node = []
        while len(current_list) > 0:
            current = current_list.pop(0)
            result.append(current.val)
            if current.left:
                leveled_node.append(current.left)
            if current.right:
                leveled_node.append(current.right)
        self.deepth += 1
        current_list.extend(leveled_node)
        self.bfs(current_list)


if __name__ == '__main__':
    t = concat_tree([3,9,20,None,None,15,7])
    s = Solution()
    print(s.maxDepth(t))
