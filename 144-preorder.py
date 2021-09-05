from typing import List

from tool import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def __dfs(r):
            if not r:
                return
            result.append(r.val)
            __dfs(r.left)
            __dfs(r.right)
        __dfs(root)
        return result
    

