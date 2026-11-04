class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        streak = 1
        for num in numSet:
            if (num-1) not in numSet:
                streak = 1
            if num+1 in numSet:
                streak += 1
                longest = max(streak, longest)
        return longest