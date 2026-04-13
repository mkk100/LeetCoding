class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for e in operations:
            if e == "+":
                stack.append(stack[-1] + stack[-2])
            elif e == "C":
                stack.pop()
            elif e == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(e))
                
        return sum(stack)