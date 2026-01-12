#
#   347. Top K Frequent Elements
#   Difficulty: Medium
#   Link: https://leetcode.com/problems/top-k-frequent-elements/
#   Description: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#   Input: nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
#
#   Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#   Output: [1,2]
#

from collections import defaultdict
from typing import List

class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # counts
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        
        # setup buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        # append highest frequency numbers first (starting from back)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for element in buckets[i]:
                res.append(element)
                if len(res) == k:
                    return res
        return []

if __name__ == "__main__":
    solution = Solution()
    top_k = solution.top_k_frequent([1,2,2,3,3,3], 2)
    print(top_k)
