class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord("a")] += 1
            res[tuple(charCount)].append(s)
    
        return res.values()

# Time complexity: O(m * n * 26) m is the element iteration, n is char iteration,  26 is populating the ascii charCount array
# Space Complexity: O(n * 26) for storing the longest word in the list