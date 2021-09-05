
"""

根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and len(token)>1):
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                if token == '+':
                    stack.append(first+second)
                elif token == '-':
                    stack.append(second-first)
                elif token == '*':
                    stack.append(second*first)
                else:
                    mul = 1
                    if second/first < 0:
                        mul = -1
                    stack.append(mul * (abs(second) // abs(first) ))
        return stack[0]


if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    print(Solution().evalRPN(tokens))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(tokens))