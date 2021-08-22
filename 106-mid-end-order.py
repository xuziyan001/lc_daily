#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]

from typing import List

from tool import TreeNode, concat_tree


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index = dict()
        n = len(inorder)
        for i, val in enumerate(inorder):
            index[val] = i

        def build(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_end-inorder_start < 0 or postorder_end - postorder_start < 0:
                return None
            root = TreeNode(postorder[postorder_end])
            idx = index[postorder[postorder_end]]
            left_length = idx-inorder_start

            left = build(inorder_start, inorder_start+left_length-1, postorder_start, postorder_start+left_length-1)
            right = build(inorder_start+left_length+1, inorder_end, postorder_start+left_length, postorder_end-1)
            root.left = left
            root.right = right
            return root

        return build(0, n-1, 0, n-1)


if __name__ == '__main__':
    inorder = [9,3,15,20,7]; postorder = [9,15,7,20,3]
    result = Solution().buildTree(inorder, postorder)
    print(result)
    ## Output: [3, 9, 20, None, None, 15, 7]