class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 1. Collect ONLY the empty cells and populate your sets
        empty_cells = []
        for r in range(9):
            for c in range(9):
                box = (r // 3) * 3 + (c // 3)
                if board[r][c] == '.':
                    empty_cells.append((r, c, box))
                else:
                    digit = board[r][c]
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)

        def valid(r, c, digit, box):
            return digit not in rows[r] and digit not in cols[c] and digit not in boxes[box]
        
        def place(r, c, digit, box):
            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)
        
        def remove(r, c, digit, box):
            board[r][c] = '.'
            rows[r].remove(digit)
            cols[c].remove(digit)
            boxes[box].remove(digit)

        # 2. Track an index pointing to our empty_cells list
        def backtrack(cell_idx):
            # Base Case: If we processed all empty cells, we are done!
            if cell_idx == len(empty_cells):
                return True
            
            # Instantly get the next cell that actually needs a number
            r, c, box = empty_cells[cell_idx]
            
            for digit in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                if valid(r, c, digit, box):
                    place(r, c, digit, box)
                    
                    # Move directly to the NEXT empty cell
                    if backtrack(cell_idx + 1):
                        return True
                    
                    remove(r, c, digit, box)
                    
            return False

        backtrack(0)
