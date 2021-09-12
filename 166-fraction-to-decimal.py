"""
给定两个整数，分别表示分数的分子numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。

"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        flag = ''
        if (numerator > 0 > denominator) or (numerator < 0 < denominator):
            flag = '-'
        par, remainder = divmod(abs(numerator), abs(denominator))
        if remainder == 0:
            return flag+str(par)
        dot = '.'
        remainder_dict = dict()
        fraction = []
        while remainder != 0:
            if remainder in remainder_dict:
                pos = remainder_dict[remainder]
                fraction.insert(pos, '(')
                fraction.append(')')
                break
            remainder_dict[remainder] = len(fraction)
            remainder *= 10
            part, remainder = divmod(abs(remainder), abs(denominator))
            fraction.append(str(part))

        return flag+str(par)+dot+''.join(fraction)


if __name__ == '__main__':
    print(Solution().fractionToDecimal(3,14))