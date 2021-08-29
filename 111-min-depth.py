# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。


from tool import TreeNode, concat_tree


class Solution:
    def __init__(self):
        self.min_depth = 1000

    def minDepth(self, root: TreeNode) -> int:

        def minDepthRecursive(node: TreeNode, current_depth: int):
            if not node:
                if self.min_depth > current_depth:
                    self.min_depth = current_depth
                    return
            if node.left is None and node.right is None:
                if self.min_depth > current_depth+1:
                    self.min_depth = current_depth+1
            current_depth += 1
            if node.left:
                minDepthRecursive(node.left, current_depth)
            if node.right:
                minDepthRecursive(node.right, current_depth)
        minDepthRecursive(root, 0)
        return self.min_depth


if __name__ == '__main__':
    t = concat_tree([3,9,20,None,None,15,7])
    r = Solution().minDepth(t)
    print(r)
    t = concat_tree([None])
    r = Solution().minDepth(t)
    print(r)
    t = concat_tree([0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,0])
    r = Solution().minDepth(t)
    print(r)