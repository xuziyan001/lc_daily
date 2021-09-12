"""
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mul = 1
        total = 0
        n = len(columnTitle)
        for i in range(n-1, -1, -1):
            total += (ord(columnTitle[i]) - 64) * mul
            mul *= 26
        return total


if __name__ =='__main__':
    print(Solution().titleToNumber('A'))