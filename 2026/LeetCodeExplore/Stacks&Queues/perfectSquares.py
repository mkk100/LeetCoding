class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = set()
        i = 1
        while i * i <= n:
            squares.add(i * i)
            i += 1
        
        q = deque([n])
        visit = set()
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                num = q.popleft()
                for s in squares:
                    remainder = num - s
                    if remainder == 0:
                        return steps
                    if remainder > 0 and remainder not in visit:
                        q.append(remainder)
                        visit.add(remainder)
        