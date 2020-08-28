class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        return self.fib_helper(N - 2, 0, 1)
        
    def fib_helper(self, N, a, b):
        c = a + b
        if N == 0:
            return c
        return self.fib_helper(N - 1, b, c)