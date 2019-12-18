class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 0
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i+1 < len(s) and roman_map[s[i+1]] > roman_map[s[i]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
