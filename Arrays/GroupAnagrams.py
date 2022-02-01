'''
Refer to awesome solution; must look!!!!!
https://leetcode.com/problems/group-anagrams/solution/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
 different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''


from collections import defaultdict
import itertools

class Solution:
    #My implementation -> itertools permutation clumsy and doesn't work for edge cases

    def groupAnagrams(self, strs):
        if len(strs) <= 1: return [strs]
        hashtable = {}
        group_anagrams = []
        for elem in strs:
            if elem in hashtable: continue
            anagrams = []
            elem_anagrams = list(itertools.permutations(elem))
            print(len(elem_anagrams))
            for elem_anag in elem_anagrams:
                anag_str = ''.join(elem_anag)
                if anag_str in strs and anag_str not in anagrams:
                    anagrams.append(anag_str)
                    hashtable[anag_str] = 1
            if len(anagrams) > 0: group_anagrams.append(anagrams)
        return group_anagrams

    def groupAnagrams_AwesomeLeetCodeSolution(self, strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                print(ord(c) - ord('a'))
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

tests = [[""],["",""],["eat","tea","tan","ate","nat","bat"]]
for test in tests:
    solve = Solution()
    print(f'Group Anagram for group {test} is {solve.groupAnagrams(test)}')