class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l,r]
            elif s < target:
                l += 1
            elif s > target:
                r -= 1