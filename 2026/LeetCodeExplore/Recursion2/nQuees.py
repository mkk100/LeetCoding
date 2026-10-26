class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols, diag, antiDiag = set(), set(), set()
        queens = []  # queens[row] = col
        res = []

        def is_not_under_attack(row, col):
            return col not in cols and row - col not in diag and row + col not in antiDiag

        def place_queen(row, col):
            cols.add(col)
            diag.add(row - col)
            antiDiag.add(row + col)
            queens.append(col)

        def remove_queen(row, col):
            cols.remove(col)
            diag.remove(row - col)
            antiDiag.remove(row + col)
            queens.pop()

        def backtrack_nqueen(row=0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        board = ["." * c + "Q" + "." * (n - c - 1) for c in queens]
                        res.append(board)
                    else:
                        backtrack_nqueen(row + 1)
                    remove_queen(row, col)

        backtrack_nqueen()
        return res