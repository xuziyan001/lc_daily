#

from tool import TreeNode, concat_tree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root]
        while stack:
            current = stack[0]
            stack = stack[1:]
            if abs(self.heightOfTree(current.left) - self.heightOfTree(current.right)) > 1:
                return False
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return True

    def heightOfTree(self, root: TreeNode):
        if not root:
            return 0
        return max(self.heightOfTree(root.left), self.heightOfTree(root.right))+1


if __name__ == '__main__':
    l = [3,9,20,None,None,15,7]
    r = concat_tree(l)
    s = Solution().isBalanced(r)
    print(s)
    l = [1,2,2,3,3,None,None,4,4]
    r = concat_tree(l)
    s = Solution().isBalanced(r)
    print(s)
    l = [1,2,2,3,None,None,3,4,None,None,4]
    r = concat_tree(l)
    print(r)
    s = Solution().isBalanced(r)
    print(s)