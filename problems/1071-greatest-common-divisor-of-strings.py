"""
tag: array
difficulty: easy
link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
description: For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times). Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
hint: If a GCD string exists, str1 + str2 equals str2 + str1; then take the prefix of length gcd(|str1|, |str2|).
"""

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: gcd(len(str1), len(str2))]


def test_1():
    assert Solution().gcdOfStrings("ABCABC", "ABC") == "ABC"


def test_2():
    assert Solution().gcdOfStrings("ABABAB", "ABAB") == "AB"

def test_3():
    assert Solution().gcdOfStrings("LEFT", "CODE") == ""
