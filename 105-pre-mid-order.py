# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归思路
from typing import List

from tool import TreeNode, concat_tree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = dict()
        n = len(preorder)
        for i, val in enumerate(inorder):
            index[val] = i

        def build(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_end-preorder_start < 0 or inorder_end - inorder_start < 0:
                return None
            root = TreeNode(preorder[preorder_start])
            idx = index[preorder[preorder_start]]
            left_length = idx-inorder_start

            left = build(preorder_start+1, preorder_start+1+left_length, inorder_start, idx-1)
            right = build(preorder_start+1+left_length, preorder_end, idx+1, inorder_end)
            root.left = left
            root.right = right
            return root

        return build(0, n-1, 0, n-1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]; inorder = [9, 3, 15, 20, 7]
    result = Solution().buildTree(preorder, inorder)
    print(result)
    ## Output: [3, 9, 20, None, None, 15, 7]

