from typing import List

from tool import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def __dfs(r):
            if not r:
                return
            __dfs(r.left)
            __dfs(r.right)
            result.append(r.val)

        __dfs(root)
        return result


