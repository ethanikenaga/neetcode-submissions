class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for z in range(i+2, len(nums)):
                    if(nums[i] + nums[j] + nums[z] == 0):
                        nums.sort()
                        if(nums not in res):
                            res.append([nums[i],nums[j],nums[z]])
        return res
        