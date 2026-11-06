import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        while i:
            res = 0
            for j in piles:
                res += math.ceil(j / i)
            if res < h:
                return i
            i += 1


        