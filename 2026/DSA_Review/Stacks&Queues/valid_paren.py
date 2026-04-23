class Solution:
    def isValid(self, s: str) -> bool:
        parenDict = {"}":"{","]":"[",")":"("}
        stack = []
        for p in s:
            if p in parenDict:
                if stack and parenDict[p] == stack[-1]: # stack: [(], p = ), parenDict[)] = (
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not len(stack)