#
#   217. Contains Duplicate
#   Difficulty: Easy
#   Link: https://leetcode.com/problems/contains-duplicate/
#   Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#   Input: nums = [1,2,3,1]
#   Output: true
#
#   Input: nums = [1,2,3,4]
#   Output: false
#
#   Input: nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    solution = Solution()
    print(solution.contains_duplicate([1,2,3,1]))
