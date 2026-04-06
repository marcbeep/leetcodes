"""
tag: array
difficulty: easy
link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
hint: Find max(candies) once; kid i wins if candies[i] + extraCandies >= that max.
"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        most = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= most)

        return result


def test_1():
    assert Solution().kidsWithCandies([2,3,5,1,3], 3) == [True, True, True, False, True]


def test_2():
    assert Solution().kidsWithCandies([4,2,1,1,2], 1) == [True, False, False, False, False]


def test_3():
    assert Solution().kidsWithCandies([12,1,12], 10) == [True, False, True]
