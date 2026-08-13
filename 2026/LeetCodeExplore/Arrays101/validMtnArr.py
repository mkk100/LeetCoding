class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        validMtn = False
        
        for i in range(1, len(arr)):
            if i < len(arr) and arr[i] > arr[i - 1] and arr[i + 1] < arr[i]: # pivotal pt
                validMtn = True
            elif validMtn == True and arr[i+1] >= arr[i]:
                return False
        return validMtn

# initial approach, this is a local check, doesn't cover globals
# approach bad 

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        i = 0
        walkUp = False
        walkDown = False
        
        while i + 1 < len(arr) and arr[i + 1] > arr[i]:
            i += 1
            walkUp = True
        
        while i + 1 < len(arr) and arr[i + 1] < arr[i]:
            i += 1
            walkDown = True
        
        return walkUp and walkDown and i == len(arr) - 1
            
