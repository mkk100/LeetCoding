class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        d_to_c = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i , curS):
            if len(digits) == len(curS):
                res.append(curS)
                return
            
            curDigit = digits[i]
            
            for c in d_to_c[curDigit]:
                backtrack(i + 1, curS + c)
                
        backtrack(0, "")
        return res