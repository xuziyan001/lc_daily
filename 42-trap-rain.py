from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        i = 0
        j = len(height) - 1
        result = 0
        left_max = height[i]
        right_max = height[j]
        while j > i:
            if left_max > right_max:
                j -= 1
                if height[j] < right_max:
                    result += right_max - height[j]
                else:
                    right_max = height[j]
            else:
                i += 1
                if height[i] < left_max:
                    result += left_max - height[i]
                else:
                    left_max = height[i]
        return result


if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([0,1]))
    print(Solution().trap([0]))
