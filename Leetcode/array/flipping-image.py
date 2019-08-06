class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        r, c = len(A), len(A[0])
        B = [[0] * c for _ in range(r)]
        
        for i in range(r):
            B[i] = A[i][::-1]
            for j in range(c):
                if B[i][j] == 0:
                    B[i][j] = 1
                else:
                    B[i][j] = 0
            
        return B
        
# Time: O(R * C)
# Space: O(R * C)