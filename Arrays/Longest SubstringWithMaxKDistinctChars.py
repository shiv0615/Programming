'''
Problem Statement#
Given a string, find the length of the longest substring in it with no more than K distinct characters.
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/solution/
Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

'''
import math

def longest_substring_with_k_distinct(str1, k):
    if len(str1) < k: return 0
    maxlen = -math.inf
    window_start = 0
    substr = []
    count_dict = {}
    distinct_char_count = 0
    for ichar, char in enumerate(str1):
        if char not in count_dict:
            count_dict[char] = 0
            distinct_char_count += 1
        else:
            count_dict[char] += 1
        if distinct_char_count <= k:
            substr.append(char)
            maxlen = max(maxlen,len(substr))
        else:
            while distinct_char_count <= k:
                substr.remove(str1[window_start])
                count_dict[char]-=1
                if count_dict[char] > 0:
                    window_start+=1
                else:
                    distinct_char_count-=1
    return ''.join(substr)

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()