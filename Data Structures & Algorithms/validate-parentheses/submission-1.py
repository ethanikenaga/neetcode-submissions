class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True