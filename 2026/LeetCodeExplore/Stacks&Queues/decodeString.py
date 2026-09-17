class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, final = [], ""
        for i in range(len(s)):
            if s[i] == "]":
                # string processing phase
                # get the string
                noOfIterations, string, num = 0, "", ""
                pieces = []
                while True:
                    popped_val = stack.pop()
                    if popped_val == "[":
                        break
                    pieces.append(popped_val)
                pieces.reverse()
                string = "".join(pieces)
                
                # get the number
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                noOfIterations = int(num[::-1])

                # adding it back to the stack
                res = string * noOfIterations
                stack.append(res)
            else:
                stack.append(s[i])
        
        while stack:
            final += stack.pop()[::-1]

        return final[::-1]
                
        