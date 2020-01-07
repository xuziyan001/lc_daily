from typing import List

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        forward = 0
        n = len(digits)
        for i in range(n-1, -1, -1):
            if i == n-1:
                forward, digits[i] = divmod(1+digits[i], 10)
            else:
                forward, digits[i] = divmod(forward+digits[i], 10)
        if forward:
            digits.insert(0, forward)
        return digits


if __name__ == '__main__':
    l = [1,2,3]
    print(Solution().plusOne(l))
    l = [1,9,9]
    print(Solution().plusOne(l))
    l = [9,9,9]
    print(Solution().plusOne(l))
    l = [0]
    print(Solution().plusOne(l))
    l = [0]
