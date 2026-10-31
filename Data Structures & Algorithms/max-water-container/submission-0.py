class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        height = 0
        for i, val in enumerate(heights):
            for j, val2 in enumerate(heights[1:], start = 1):
                height = min(val,val2)
                width = j-i
                if((height * width) >max):
                    max = height*width
        return max
                

        