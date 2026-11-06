import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = (right-left) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/middle)
            if hours < h:
                right = middle
            if hours >= h:
                left = middle + 1
        return left