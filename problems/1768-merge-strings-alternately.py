"""
tag: array
difficulty: easy
link: https://leetcode.com/problems/merge-strings-alternately
hint: Use two pointers and alternate between each string until both are exhausted.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = ""
        
        while i < len(word1) or j < len(word2):
            
            if i < len(word1):
                result += word1[i]
                i += 1

            if j < len(word2):
                result += word2[j]
                j += 1
        
        return result 

def test_1():
    assert Solution().mergeAlternately("abc", "pqr") == "apbqcr"


def test_2():
    assert Solution().mergeAlternately("ab", "pqrs") == "apbqrs"


def test_3():
    assert Solution().mergeAlternately("abcd", "pq") == "apbqcd"
