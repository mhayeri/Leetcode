#
#   1. Two Sum
#   Difficulty: Easy
#   Link: https://leetcode.com/problems/two-sum/
#   Description: Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#                You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#                Return the answer with the smaller index first.
#
#   Input: nums = [3,4,5,6], target = 7
#   Output: [0,1]
#
#   Input: nums = [4,5,6], target = 10
#   Output: [0,2]
#
#   Input: nums = [5,5], target = 10
#   Output: [0,1]

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        pairs = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in pairs:
                return [pairs[compliment], idx]
            pairs[num] = idx
        return [-1, -1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([1,2,3,7], 10))
