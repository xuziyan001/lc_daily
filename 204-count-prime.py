import math


class Solution:
    def countPrimes2(self, n: int) -> int:
        def is_prime(t):
            if t <= 1:
                return False
            if t == 2:
                return True
            m = int(math.sqrt(t))
            for ii in range(2, m+1):
                if t % ii == 0:
                    return False
            return True
        count = 0
        for i in range(2, n):
            if is_prime(i):
                count += 1
        return count
    # 厄拉多塞筛法，简称埃氏筛
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1
                for j in range(2*i, n, i):
                    isPrime[j] = False
        return cnt




if __name__ == '__main__':
    print(Solution().countPrimes(10000))