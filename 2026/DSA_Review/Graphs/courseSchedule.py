class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites: # set up the hashMap for courses and its prereqs
            preMap[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs) # to detect cycle
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = [] # if crs can be completed, empty it to skip work
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True