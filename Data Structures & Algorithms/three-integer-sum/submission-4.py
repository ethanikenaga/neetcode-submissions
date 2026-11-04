class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for z in range(j + 1, len(nums)):
                    if(nums[i] + nums[j] + nums[z] == 0):
                        temp = [nums[i],nums[j],nums[z]]
                        temp.sort()
                        res.add(temp)
        return [list(i) for i in res]
        