"""
tag: array
difficulty: easy
link: https://leetcode.com/problems/can-place-flowers/
hint: Greedily plant in the first valid slot; n is how many are left to place, so succeed iff n <= 0.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            ):
                flowerbed[i] = 1
                n -= 1
        return n <= 0

def test_1():
    assert Solution().canPlaceFlowers([1,0,0,0,1], 1) == True


def test_2():
    assert Solution().canPlaceFlowers([1,0,0,0,1], 2) == False