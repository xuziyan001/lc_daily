"""
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 0:
            return ""
        res = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber, 26)
            if remainder == 0:
                res.append(26)
                columnNumber -= 1
            else:
                res.append(remainder)
        res.reverse()
        for i in range(len(res)):
            res[i] = chr(64+res[i])
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().convertToTitle(677))