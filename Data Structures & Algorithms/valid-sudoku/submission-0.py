from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True

        boxes = defaultdict(set)
        rows = defaultdict(set)
        columns = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                boxrow = row // 3
                boxcol = col // 3

                box = boxrow * 3 + boxcol

                if cell in boxes[box] or cell in rows[row] or cell in columns[col]:
                    return False
                
                boxes[box].add(cell)
                columns[col].add(cell)
                rows[row].add(cell)
        
        return True