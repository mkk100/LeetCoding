# recursive
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(cur, openC, closeC):
            if len(cur) == 2*n:
                res.append(cur)
                return

            if openC < n:
                backtrack(cur + "(", openC + 1, closeC)
            if closeC < openC:
                backtrack(cur + ")", openC, closeC + 1)
                
        backtrack("", 0, 0)
        return res
        

# iterative
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []
        stack.append(("", 0, 0))
        
        while stack:
            cur, openC, closeC = stack.pop()
            
            if openC == closeC == n:
                res.append(cur)
                continue
            
            if openC < n:
                stack.append((cur + "(",openC + 1, closeC))
            if closeC < openC:
                stack.append((cur + ")", openC, closeC + 1))
        return res
        
                        
