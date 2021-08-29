
from tool import TreeNode, concat_tree


class Solution(object):
    def hasPathSum(self, root, targetSum):
        def currentSum(t, numSum):
            if not t:
                return False
            if numSum + t.val == targetSum:
                if t.left is None and t.right is None:
                    return True
            return currentSum(t.left, numSum + t.val) or currentSum(t.right, numSum + t.val)
        return currentSum(root, 0)


if __name__ == '__main__':
    l = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    t = concat_tree(l)
    r = Solution().hasPathSum(t, 22)
    print(r)
