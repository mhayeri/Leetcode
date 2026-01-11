#
#   49. Group Anagrams
#   Difficulty: Medium
#   Link: https://leetcode.com/problems/group-anagrams/
#   Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#   Input: strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
#   Input: strs = [""]
#   Output: [[""]]
#
#   Input: strs = ["a"]
#   Output: [["a"]]

from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1

            key = tuple(key)
            ans[key].append(s)
        
        return list(ans.values())

if __name__ == "__main__":
    solution = Solution()
    print(solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]))
