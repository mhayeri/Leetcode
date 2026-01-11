#
#   271. Encode and Decode Strings
#   Difficulty: Medium
#   Link: https://leetcode.com/problems/encode-and-decode-strings/
#   Description: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#                Implement the encode and decode methods.
#                You are not allowed to solve the problem using any serialize methods (such as eval).
#
#   Input: dummy_input = ["Hello","World"]
#   Output: ["Hello","World"]
#

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

if __name__ == "__main__":
    solution = Solution()
    encode = solution.encode(["Hello","World"])
    decode = solution.decode(encode)
    print(encode)
    print(decode)
