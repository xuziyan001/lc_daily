# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

from typing import List

import copy

from tool import TreeNode, concat_tree


class Solution:
    def __init__(self):
        self.total_result = []
        self.direction = True

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
        if not self.direction:
            result.reverse()
        self.direction = not self.direction

        self.total_result.append(result)
        current_list.extend(leveled_node)
        self.bfs(current_list)


if __name__ == '__main__':
    t = concat_tree([3,9,20,None,None,15,7])
    s = Solution()
    print(s.zigzagLevelOrder(t))