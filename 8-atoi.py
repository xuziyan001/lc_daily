class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        INTMAX = pow(2,31)-1
        INTMIN = -pow(2,31)
        is_pos = 1
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                is_pos = -1
            s = s[1:]
        result = '0'
        for each in s:
            if each.isdigit():
                result += each
            else:
                break
        toi = int(result) * is_pos
        if toi > INTMAX or toi < INTMIN:
            return INTMAX if is_pos == 1 else INTMIN
        return toi


if __name__ == '__main__':
    print(Solution().myAtoi('-91283472332'))
    print(Solution().myAtoi('words and 987'))
    print(Solution().myAtoi('4193 with words'))
