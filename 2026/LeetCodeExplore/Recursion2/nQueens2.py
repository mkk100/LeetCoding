class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols, diag, antiDiag = set(), set(), set()

        def is_not_under_attack(row,col):
            return col not in cols and row - col not in diag and row + col not in antiDiag

        def place_queen(row,col):
            cols.add(col)
            diag.add(row - col)
            antiDiag.add(row + col)

        def remove_queen(row,col):
            cols.remove(col)
            diag.remove(row - col)
            antiDiag.remove(row + col)

        def backtrack_nqueen(row = 0, count = 0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return count
        return backtrack_nqueen(0,0)