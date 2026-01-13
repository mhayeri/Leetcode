#
#   238. Product of Array Except Self
#   Difficulty: Medium
#   Link: https://leetcode.com/problems/top-k-frequent-elements/
#   Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#                The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#                You must write an algorithm that runs in O(n) time and without using the division operation.
#
#   Input: nums = [1,2,3,4]
#   Output: [24,12,8,6]
#
#   Input: nums = [-1,1,0,-3,3]
#   Output: [0,0,9,0,0]
#

from collections import defaultdict
from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        for i in range(1, len(nums)):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        right_products = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
    
        return [x*y for x,y in zip(left_products, right_products)]

if __name__ == "__main__":
    solution = Solution()
    product = solution.product_except_self([1,2,3,4])
    print(product)
