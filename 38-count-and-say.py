class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        start = "1"
        for i in range(2, n+1):
            l = len(start)
            result = []
            j = 0
            current = start[j]
            count = 1
            j += 1
            while j < l:
                if start[j] == current:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(current)
                    current = start[j]
                    count = 1
                j += 1
            result.append(str(count))
            result.append(current)
            start = ''.join(result)
        return start


if __name__ == '__main__':
    print(Solution().countAndSay(2))
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
    print(Solution().countAndSay(6))
    print(Solution().countAndSay(7))




