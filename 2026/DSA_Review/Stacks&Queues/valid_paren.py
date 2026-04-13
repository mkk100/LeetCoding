class Solution:
    def isValid(self, s: str) -> bool:
        parenDict = {")":"(", "}":"{","]":"["}
        stack = []
        for p in s:
            if p in parenDict:
                if stack and stack[-1] == parenDict[p]: # ( != ], check matching parentheses                   
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not len(stack)
