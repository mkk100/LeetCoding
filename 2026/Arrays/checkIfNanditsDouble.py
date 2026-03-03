# use a set, second condition is to check if the number is even and already seen
# there are 3 other approaches, maybe you can take a look at them.
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        
        for num in arr:
            if num*2 in seen:
                return True
            if num % 2 == 0 and num // 2 in seen:
                return True
            seen.add(num)
        return False