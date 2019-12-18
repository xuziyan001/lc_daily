class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        i = 0
        result = []
        while num != 0:
            remain = num % 10
            num //= 10
            if remain <= 3:
                result.append(roman_list[2*i]*remain)
            elif remain == 4:
                result.append(roman_list[2*i]+roman_list[2*i+1])
            elif remain == 9:
                result.append(roman_list[2*i]+roman_list[2*i+2])
            else:
                result.append(roman_list[2*i+1]+roman_list[2*i]*(remain-5))
            i += 1
        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    print(Solution().intToRoman(1994)) # MCMXCIV
    print(Solution().intToRoman(0)) # MCMXCIV
