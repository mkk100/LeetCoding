class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashMap = []
        count = 0
        for word in words:
            alphabetArr = set()
            for a in word:
                if a not in alphabetArr:
                    alphabetArr.add(a)
            if alphabetArr not in hashMap:
                hashMap.append(alphabetArr)
            else:
                count += 1
        return count
# gotta come back