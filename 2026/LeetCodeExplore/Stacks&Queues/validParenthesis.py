class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren = {")":"(","}":"{","]":"["}
        stack = []
        for p in s:
            if p in paren:
                if stack and stack[-1] == paren[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0
                