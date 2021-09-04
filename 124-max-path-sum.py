"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

"""

from tool import TreeNode, concat_tree


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -1000000
        def maxGain(r):
            if not r:
                return 0
            #m = r.val+maxGain(r.left)+maxGain(r.right)
            ll = max(maxGain(r.left), 0)
            rr = max(maxGain(r.right), 0)
            m = r.val + ll + rr
            if m > self.max_sum:
                self.max_sum = m
            # 以r为起点，计算最大贡献值
            return r.val + max(ll, rr)
        maxGain(root)

        return self.max_sum


if __name__ == '__main__':
    l = concat_tree([1,2,3])
    print(Solution().maxPathSum(l))
    l = concat_tree([-10,9,20,None,None,15,7])
    print(Solution().maxPathSum(l))
    l = concat_tree([-2,-1])
    print(Solution().maxPathSum(l))
    l = concat_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(l)
    print(Solution().maxPathSum(l))
