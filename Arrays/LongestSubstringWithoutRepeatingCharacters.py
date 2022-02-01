'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        charset = {}
        nonrepeating = []
        maxlen = -9999
        window_start = 0
        for indx, char in enumerate(s):
            if char not in charset or charset[char] == 0:
                nonrepeating.append(char)
                maxlen = max(len(nonrepeating), maxlen)
                charset[char] = 1
            else:
                nonrepeating.append(char)
                charset[char] += 1
                for i in range(window_start, indx, 1):
                    if charset[s[i]] > 1: break
                for i in range(window_start, i + 1, 1):
                    nonrepeating.remove(s[i])
                    charset[s[i]] -= 1
                window_start = i + 1
        return max(maxlen, len(nonrepeating))

# Test Strings
tests = ["tmmzuxt","dvdf","pwwkew","abcabcbb"]
for test in tests:
    sol = Solution()
    print(f'Longest Substring for String {test} is {sol.lengthOfLongestSubstring(s=test)}')