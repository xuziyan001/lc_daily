# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。


from tool import TreeNode, concat_tree

class Solution:
    def __init__(self):
        self.min = 1000

    def minDepth(self, root: TreeNode) -> int:

        def minDepthRecursive(node: TreeNode, current_depth: int) -> int:
            if not TreeNode:
                return current_depth
            if node.left is None and node.right is None:
                if self.min_depth > current_depth+1:
                    self.min_depth = current_depth+1
                return current_depth+1
            return max(minDepthRecursive(node.left, current_depth), minDepthRecursive(node.right, current_depth))+1
        return self.min