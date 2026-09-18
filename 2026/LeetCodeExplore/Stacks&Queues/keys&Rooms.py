class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        hashSet = set()
        def dfs(key):
            if key in hashSet:
                return True
            hashSet.add(key)
            
            for room in rooms[key]:
                dfs(room)
        dfs(0)
        return len(hashSet) == len(rooms)
        