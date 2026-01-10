#
#   242. Valid Anagram
#   Difficulty: Easy
#   Link: https://leetcode.com/problems/valid-anagram/
#   Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#   Input: s = "anagram", t = "nagaram"
#   Output: true
#
#   Input: s = "rat", t = "car"
#   Output: false
#

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        _len = len(s)
        for i in range(_len):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        for i in counts:
            if i != 0:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram("anagram", "nagaram"))
