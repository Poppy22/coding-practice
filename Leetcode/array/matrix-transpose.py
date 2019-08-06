
# In place for square matrix
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R, C = len(A), len(A[0])
        
        for r in range(R):
            for c in range(r):
                A[c][r], A[r][c] = A[r][c], A[c][r]
                
        return A

# Time: O(R ^ 2)
# Space: O(1)


# Non-square matrix
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R, C = len(A), len(A[0])
        T = [[0] * R for _ in range(C)]
        for r in range(R):
            for c in range(C):
                T[c][r] = A[r][c]
               
        return T

# Time: O(R * C)
# Space: O(R * C)