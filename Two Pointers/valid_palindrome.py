#
#   125. Valid Palindrome
#   Difficulty: Easy
#   Link: https://leetcode.com/problems/valid-palindrome/
#   Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
#                non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#                Given a string s, return true if it is a palindrome, or false otherwise.
#
#   Input: s = "A man, a plan, a canal: Panama"
#   Output: true
#
#   Input: s = "race a car
#   Output: false

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.valid_palindrome("Was it a car or a cat I saw?"))
