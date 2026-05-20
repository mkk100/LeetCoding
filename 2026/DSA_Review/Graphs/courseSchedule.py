class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites: # set up the hashMap for courses and its prereqs to dfs
            preMap[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs) # for cycle detection for incompletable courses
            for pre in preMap[crs]: # loop thru the pre reqs and dfs on pre reqs
                if not dfs(pre):
                    return False # means not completable
            visit.remove(crs)
            preMap[crs] = [] # if crs can be completed, empty it to skip work
            return True
        
        for crs in range(numCourses): # call it for every single course
            if not dfs(crs):
                return False
        return True

# May 20th