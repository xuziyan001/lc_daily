import copy

from tool import TreeNode, concat_tree


class Solution(object):
    def hasPathSum(self, root, targetSum):
        result = []
        def currentSum(t, numSum, stack):
            stack.append(t.val)
            if t.left is None and t.right is None:
                if numSum+t.val == targetSum:
                    result.append(stack)
                    return True
                else:
                    return False
            if t.left:
                currentSum(t.left, numSum + t.val, copy.copy(stack))
            if t.right:
                currentSum(t.right, numSum + t.val, copy.copy(stack))
        if not root:
            return result
        currentSum(root, 0, [])
        return result


if __name__ == '__main__':
    l = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    t = concat_tree(l)
    r = Solution().hasPathSum(t, 22)
    print(r)
    l = [None]
    t = concat_tree(l)
    r = Solution().hasPathSum(t, 1)
    print(r)
