class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = "+/*-" # this faster than set
        for t in tokens:
            if t in operators:
                f = int(stack.pop())
                s = int(stack.pop())
                if t == "+":
                    stack.append(f + s)
                elif t == "-":
                    stack.append(s-f) # be careful of this
                elif t == "*":
                    stack.append(f * s)
                elif t == "/":
                    stack.append(int(s / float(f))) # and this
            else:
                stack.append(int(t))
        return stack[-1]
                    
            