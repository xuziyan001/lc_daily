class Solution:
    def addBinary(self, a: str, b: str) -> str:
        forward = 0
        m = len(a)
        n = len(b)
        mm = max(m, n)
        a = list('0'*(mm-m) + a)
        b = list('0'*(mm-n) + b)
        for i in range(mm-1, -1 ,-1):
            forward, t = divmod(int(a[i])+int(b[i])+forward, 2)
            a[i] = str(t)
        if forward:
            a.insert(0, str(forward))
        return ''.join(a)


if __name__ == '__main__':
    print(Solution().addBinary("11",'1'))
    print(Solution().addBinary("1010",'1011'))
