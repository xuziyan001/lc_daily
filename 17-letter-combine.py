from typing import List


class Solution:
    number_dic = {
        '2': 'a b c',
        '3': 'd e f',
        '4': 'g h i',
        '5': 'j k l',
        '6': 'm n o',
        '7': 'p q r s',
        '8': 't u v',
        '9': 'w x y z',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return Solution.number_dic[digits[0]].split()
        else:
            remains = self.letterCombinations(digits[1:])
            result = []
            for each in Solution.number_dic[digits[0]].split():
                for r in remains:
                    result.append(each + r)
            return result


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
