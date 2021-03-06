# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

from typing import List

import copy

from tool import TreeNode, concat_tree


class Solution:
    def __init__(self):
        self.total_result = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.bfs([root])
        return self.total_result

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
        self.total_result.append(result)
        current_list.extend(leveled_node)
        self.bfs(current_list)


if __name__ == '__main__':
    t = concat_tree([3,9,20,None,None,15,7])
    s = Solution()
    print(s.levelOrder(t))
    t = concat_tree([None])
    s = Solution()
    print(s.levelOrder(t))
    t = concat_tree([1])
    s = Solution()
    print(s.levelOrder(t))
    t = concat_tree([1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5])
    print(t)
    s = Solution()
    print(s.levelOrder(t))
