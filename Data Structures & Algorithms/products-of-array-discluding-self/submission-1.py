class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for num in nums:
            if num:
                product *= num
            else:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if zero == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:
                nums[i] = int(product / nums[i])
        return nums