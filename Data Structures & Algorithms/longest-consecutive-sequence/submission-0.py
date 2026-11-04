class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        res = 1
        tmp = 1
        while len(nums) > 1:
            val = nums.pop()
            if nums[-1] == (val-1):
                tmp +=1
            elif nums[-1] == val:
                continue
            else:
                tmp = 1
            res = max(tmp, res)
        return res
            