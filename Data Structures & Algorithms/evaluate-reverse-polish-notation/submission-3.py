class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"-","+","*","/"}:
                try:
                    int(token)
                    stack.append(token)
                except:
                    return -1
            else:
                if len(stack) < 2:
                    return -1
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "/":
                    stack.append(int(val2/val1))
                elif token == "-":
                    stack.append(val2 - val1)
                else:
                    return -1
        if len(stack) != 1:
            return -1
        return int(stack.pop())