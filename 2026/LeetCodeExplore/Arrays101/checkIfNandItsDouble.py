class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashT = set()
        for i in range(len(arr)):
            if arr[i] * 2 in hashT or (arr[i] % 2 == 0 and arr[i] / 2 in hashT):
                return True
            hashT.add(arr[i])
            # two conditions: "double of" and "half of"
        return False