class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            d[val] = i
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [d[nums[l]],d[nums[r]]]
            elif s < target:
                l += 1
            elif s > target:
                r -= 1