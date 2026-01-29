#
#   11. Container With Most Water
#   Difficulty: Medium
#   Link: https://leetcode.com/problems/container-with-most-water/
#   Description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#                Find two lines that together with the x-axis form a container, such that the container contains the most water.
#                Return the maximum amount of water a container can store.
#
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#
#   Input: height = [1,1]
#   Output: 1

from typing import List

class Solution:
    def max_area(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        _max = 0
        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            area = base * height
            _max = max(_max, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.max_area([1,8,6,2,5,4,8,3,7]))
