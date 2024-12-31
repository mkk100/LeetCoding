class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        s = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in s[(i//3, j//3)]:
                    return False
                
                r[i].add(board[i][j])
                c[j].add(board[i][j])
                s[(i//3, j//3)].add(board[i][j])
        
        return True

# Time complexity: O(n)
# Space complexity: O(n)
# tip: the ds being used here is a set, example: r -> {0: {1, 2, 3}, 1: {4, 5, 6}}, c: {0: {1, 4, 7}, 1: {2, 5, 8}}, s: {(0, 0): {1, 2, 3}, (0, 1): {4, 5, 6}}
# it's key is integer and value is set.