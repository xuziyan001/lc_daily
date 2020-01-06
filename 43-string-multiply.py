from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        l = len(num2)
        res = []
        for i in range(l-1, -1, -1):
            res.append(self.multiply_single(num1, num2[i])+"0"*(l-i-1))
        return self.add(res)

    def add(self, nums: List) -> str:
        m = max([len(num) for num in nums])
        upper = 0
        result = ''
        for i in range(m):
            s = 0
            for num in nums:
                if len(num) < i+1:
                    continue
                else:
                    s += int(num[-1-i])
            s += upper
            upper, t = divmod(s, 10)
            result = str(t) + result
        if upper > 0:
            result = str(upper) + result
        return result

    def multiply_single(self, num1: str, num2: str) -> str:
        l = len(num1)
        right = int(num2)
        upper = 0
        result = ''
        for i in range(l-1, -1, -1):
            left = int(num1[i])
            tmp = left * right + upper
            upper, tail = divmod(tmp, 10)
            result = str(tail) + result
        if upper > 0:
            result = str(upper) + result
        return result


if __name__ == '__main__':
    print(Solution().multiply_single('123333333', '9'))
    print(123333333*9)
    print(Solution().multiply('123333333', '98'))
    print(Solution().add(['986666664', '11099999970', '778667655']))
