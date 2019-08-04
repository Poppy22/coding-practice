class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        rows = {}
        columns = {}
        square = {}
        for i in range(n):
            rows[i] = {}
            columns[i] = {}
            square[i] = {}
            
        # check rows
        for i in range(n):
            for j in range(n):
                value = board[i][j]
                if value != '.':
                    if int(value) in rows[i].keys():
                        return False
                    rows[i][int(value)] = 1
                    
        # check columns
        for i in range(n):
            for j in range(n):
                value = board[j][i]
                if value != '.':
                    if int(value) in columns[i].keys():
                        return False
                    columns[i][int(value)] = 1
                    
        # check squares
        rstart = 0
        cstart = 0
        for i in range(n):
            for r in range(rstart, rstart + 3):
                for c in range(cstart, cstart + 3):
                    value = board[r][c]
                    if value != '.':
                        if int(value) in square[i].keys():
                            return False
                        square[i][int(value)] = 1
                        
            cstart += 3
            if cstart == 9:
                cstart = 0
                rstart += 3
        
        return True
        