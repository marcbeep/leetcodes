"""
tag: array
difficulty: easy
link: https://leetcode.com/problems/greatest-common-divisor-of-strings
hint: Try every prefix length from longest to shortest and check if it can build both strings.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       
        # s = abcabc, pattern = abc
        def can_build(s, pattern):

            # if 6 % 3 == 0, it might work
            if len(s) % len(pattern) != 0:
                return False

            # how many times we need to repeat pattern
            times = len(s) // len(pattern)

            # build repeated string manually
            built = ""
            for _ in range(times):
                built += pattern

            return built == s

        # Answer cannot be longer than shorter string
        max_len = min(len(str1), len(str2))

        # Try every possible prefix length from longest to shortest
        for length in range(max_len, 0, -1):
            candidate = str1[:length]

            # if cand length doesn't divide both lengths evenly, it can't build both strs
            if len(str1) % length != 0 or len(str2) % length != 0:
                continue

            if can_build(str1, candidate) and can_build(str2, candidate):
                return candidate

        return ""


def test_1():
    assert Solution().gcdOfStrings("ABCABC", "ABC") == "ABC"


def test_2():
    assert Solution().gcdOfStrings("ABABAB", "ABAB") == "AB"

def test_3():
    assert Solution().gcdOfStrings("LEFT", "CODE") == ""
