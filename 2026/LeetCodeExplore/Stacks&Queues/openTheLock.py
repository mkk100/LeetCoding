class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10) # actual adding process
                res.append(lock[:i] + digit + lock[i+1:]) # string manipulation
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q, visit = deque(), set(deadends)
        q.append(["0000", 0]) # locks, turns
        
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            
            for i in children(lock):
                if i not in visit:
                    visit.add(i)
                    q.append([i, turns + 1])
        return -1 
 
 # O(10,000) cus 10 * 10 * 10 * 10 for each lock combination           
        
        