class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return False
        if s[0] in '-+':
            s = s[1:]
        base_num = ''
        is_exp = False
        exp_num = ''
        exp_neg = False
        for c in s:
            if c.isdigit():
                if is_exp:
                    exp_num += c
                else:
                    base_num += c
            elif c == '.':
                if is_exp:
                    return False
                else:
                    if '.' in base_num:
                        return False
                    base_num += c
            elif c == 'e':
                if is_exp:
                    return False
                if len(base_num) == 0:
                    return False
                is_exp = True
            elif c in '+-':
                if not is_exp:
                    return False
                if exp_neg:
                    return False
                if len(exp_num) != 0:
                    return False
                exp_neg = True
            else:
                return False
        if is_exp and len(exp_num) == 0:
            return False
        if base_num == '.':
            return False
        return True


if __name__ == '__main__':
    s = "0"
    print(Solution().isNumber(s))
    s = " 0.1 "
    print(Solution().isNumber(s))
    s = "abc"
    print(Solution().isNumber(s))
    s = "1 a"
    print(Solution().isNumber(s))
    s = "2e10"
    print(Solution().isNumber(s))
    s = " -90e3   "
    print(Solution().isNumber(s))
    s = " 1e" # False
    print(Solution().isNumber(s))
    s = "e3"
    print(Solution().isNumber(s))
    s = " 6e-1"
    print(Solution().isNumber(s))
    s = " 99e2.5 " # false
    print(Solution().isNumber(s))
    s = "53.5e93"
    print(Solution().isNumber(s))
    s = " --6 "
    print(Solution().isNumber(s))
    s = "-+3"
    print(Solution().isNumber(s))
    s = "95a54e53"
    print(Solution().isNumber(s))
    s = ".1"
    print(Solution().isNumber(s))
    s = "."
    print(Solution().isNumber(s))
    s = "459277e38+"
    print(Solution().isNumber(s))



