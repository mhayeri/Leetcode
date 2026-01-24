#
#   128. Longest Consecutive Sequence
#   Difficulty: Medium
#   Link: https://leetcode.com/problems/longest-consecutive-sequence/
#   Description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#                You must write an algorithm that runs in O(n) time.
#
#   Input: nums = [100,4,200,1,3,2]
#   Output: 4
#
#   Input: nums = [0,3,7,2,5,8,4,6,0,1]
#   Output: 9
#

from typing import List

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        _max = 0
        _set = set(nums)
        for num in _set:
            if num - 1 not in _set:
                curr = 1
                while num + curr in _set:
                    curr += 1
                # Update max
                _max = max(_max, curr)
        return _max

if __name__ == "__main__":
    solution = Solution()
    longest = solution.longest_consecutive([0,3,7,2,5,8,4,6,0,1])
    print(longest)
