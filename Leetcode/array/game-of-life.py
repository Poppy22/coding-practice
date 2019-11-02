class Solution(object):
    def count_neighbours(self, board, i, j):
        # positions = [up, down, left, right, up-left, up-right, down-left, down-right]
        positions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        N = len(board)
        M = len(board[0])
        alive = 0
        
        for p in positions:
            if i + p[0] < 0 or i + p[0] >= N or j + p[1] < 0 or j + p[1] >= M:
                continue
            if abs(board[i + p[0]][j + p[1]]) == 1:
                alive += 1
    
        return alive
                        
                        
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 0 -> was and remained 0
        # 1 -> was and remained 1
        # -1 -> was 1 and became 0 (extracted 2)
        # -2 -> was 0 and became 1 (extracted 2)
        
        N = len(board)
        M = len(board[0])
        
        for i in range(N):
            for j in range(M):
                alive = self.count_neighbours(board, i, j)
                if board[i][j] == 1 and (alive < 2 or alive > 3):
                    board[i][j] -= 2
                if board[i][j] == 0 and alive == 3:
                    board[i][j] -= 2
                    
        for i in range(N):
            for j in range(M):
                if board[i][j] < 0:
                    board[i][j] = abs(board[i][j] + 1)
                       
               
        
        