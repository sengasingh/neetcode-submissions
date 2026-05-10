from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def getBox(r,c):
            if 0 <= r < 3:
                if 0 <= c < 3:
                    return 0
                elif 3 <= c < 6:
                    return 1
                else:
                    return 2
            elif 3 <= r < 6:
                if 0 <= c < 3:
                    return 3
                elif 3 <= c < 6:
                    return 4
                else:
                    return 5
            else:
                if 0 <= c < 3:
                    return 6
                elif 3 <= c < 6:
                    return 7
                else:
                    return 8

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue
                
                if cell in rows[row] or cell in cols[col] or cell in boxes[getBox(row,col)]:
                    return False
                
                rows[row].add(cell)
                cols[col].add(cell)
                boxes[getBox(row,col)].add(cell)
    
        return True