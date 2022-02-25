'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/solution/
211. Design Add and Search Words Data Structure
Medium

4590

189

Add to List

Share
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

from collections import OrderedDict

class WordDictionary:

    def __init__(self):
        self.d = OrderedDict()
        self.d[''] = OrderedDict()

    def addWord(self, word):
        dict = self.d['']
        for char in word:
            if char not in self.d:
                dict[char] = OrderedDict()
                dict       = dict[char]
            else:
                dict = dict[char]

    def search(self, word):
        search_word = []
        dict = self.d['']
        for char in word:
            if not char.isalnum(): continue
            if char in dict:
                dict = dict[char]
                search_word.append(char)
            else:
                return False
        search_word = ''.join(search_word)
        return search_word == word

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("badass");
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) #True
print(wordDictionary.search("b..")) #True