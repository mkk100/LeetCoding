class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {} # stores last index
        for i, c in enumerate(s):
            hashMap[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, hashMap[c])

            if i == end:
                res.append(size) 
                size = 0
        return res



        
