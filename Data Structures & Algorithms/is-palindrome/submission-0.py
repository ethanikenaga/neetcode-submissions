class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ""

        for char in s.lower():
            if(char.isalnum()):
                copy+=char
        return copy[::-1] == copy
        