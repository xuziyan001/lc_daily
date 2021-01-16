"""
给定一个二叉树，返回它的中序 遍历。
"""
from typing import List
from tool import TreeNode, concat_tree


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(r = root):
            if r is None:
                return
            traversal(r.left)
            res.append(r.val)
            traversal(r.right)
        res = []
        traversal()
        return res


if __name__ == '__main__':
    l = [1, None, 2, 3]
    t = concat_tree(l)
    #print(Solution().inorderTraversal(t))
