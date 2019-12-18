from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        # bfs?
        result = []
        for i in range(1, n+1):
            current = '('*i + ')'
            result += self.gen(current, n-i, n-1)
        return result

    def gen(self, current, left, right):
        if left > right:
            return []
        if left == right == 0:
            return []
        if left == 0 and right > 0:
            return [current + ')'*right]
        left_first = self.gen(current+'(', left-1, right)
        right_first = self.gen(current+')', left, right-1)
        return left_first+right_first


if __name__ == '__main__':
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(2))
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
    print(Solution().generateParenthesis(5))
    print(Solution().generateParenthesis(6))
