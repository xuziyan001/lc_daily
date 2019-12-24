class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max = 0
        stack = []
        current = 0
        last_fin_index = -1
        for each in range(len(s)):
            if s[each] == '(':
                stack.append(each)
            else:
                if len(stack) == 0:
                    # 提前结束
                    last_fin_index = each
                    if current > max:
                        max = current
                    current = 0
                else:
                    stack.pop()
                    current += 2
        if stack:
            stack.append(len(s))
            stack = [last_fin_index] + stack
            for j in range(len(stack)-1, 0, -1):
                gap = stack[j] - stack[j-1] - 1
                if gap > max:
                    max = gap
        else:
            if current > max:
                max = current
        return max


if __name__ == '__main__':
    print(Solution().longestValidParentheses(')()()('))
    print(Solution().longestValidParentheses('(()'))
    print(Solution().longestValidParentheses('()(()'))
    print(Solution().longestValidParentheses('()'))
    print(Solution().longestValidParentheses(")()())()()("))
    print(Solution().longestValidParentheses("(()(((()"))
    print(Solution().longestValidParentheses("(())()((("))
    print(Solution().longestValidParentheses("()(((((()()(((())())))))))())))())())()()(()))(()))()))((()))))(())(()()))((((())()()())(((()((()(())((()())"))
