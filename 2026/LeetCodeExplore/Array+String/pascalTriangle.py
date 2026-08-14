class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # hints, O(n^2), add 0s, and use two pointers on prior rows to fill out curr
        # 5, 1
        # 1
        #1, 1
        
        res, resSubArr = [],[]
        res.append([1])
        prev = [0,1,0]
        if numRows == 1:
            return res
                    
        rows, cols = numRows, 1
        
        for i in range(1, rows): # 1
            k = 0 # [0,1,0]
            while k + 1 < len(prev):
                resSubArr.append(prev[k] + prev[k+1])
                k += 1
            prev = [0] + resSubArr + [0] # [0,1,1,0]
            res.append(resSubArr)
            resSubArr = []
        return res
# my approach: added 0s and O(n^2) but no two ptrs

# same approach: optimal wiith 2 pointers
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # hints, O(n^2), add 0s, and use two pointers on prior rows to fill out curr
        # 5, 1
        # 1
        #1, 1
        
        res = [[1]]
        for i in range(numRows - 1): # -1 because we already have 1 row
            prev = [0] + res[-1] +[0]
            subArr = []
            l, r = 0, 1
            for j in range(len(res[-1]) + 1): # +1 to account for one more iteration of l + r
                subArr.append(prev[l] + prev[r])
                l += 1
                r += 1
            res.append(subArr) 
        return res

                        
                
                
                
                
                
                
                        
                
                
                
                
                
                