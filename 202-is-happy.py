"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

"""
class Solution:
    def isHappy(self, n: int) -> bool:

        def __next(n):
            s = 0
            for each in str(n):
                s += int(pow(int(each), 2))
            return s
        d = dict()
        start = n
        while start != 1 and start not in d:
            n = __next(start)
            d[start] = n
            start = n
        return start == 1


if __name__ == '__main__':
    print(Solution().isHappy(19))
