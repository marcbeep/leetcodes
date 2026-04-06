"""
tag: array
difficulty: easy
link: https://leetcode.com/problems/two-sum/
description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
hint: Use a hashmap to store seen values and check complements in one pass.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i


def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_2():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_3():
    assert Solution().twoSum([3, 3], 6) == [0, 1]
