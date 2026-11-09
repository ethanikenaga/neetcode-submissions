class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        res = 0
        for c in s:
            while c in temp:
                temp = temp[1:]
            temp += c
            res = max(len(temp), res)
        return res
            

        