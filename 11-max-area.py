from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i = 0
        j = len(height) -1
        while j != i:
            result = max(result, min(height[i],height[j])*(j-i))
            if height[i] > height[j]:
                current_min = height[j]
                j -= 1
                while j != i and height[j] < current_min:
                    j -= 1
            else:
                current_min = height[i]
                i += 1
                while j != i and height[i] < current_min:
                    i += 1
        return result


if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49
    print(Solution().maxArea([1,2,2,1])) # 3
