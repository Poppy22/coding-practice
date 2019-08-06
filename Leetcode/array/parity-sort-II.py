class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # make sure all the even numbers get to the correct position
        # and by swapping, odd numbers will also get the correct position
    
        j = 1 # odd position contor
        i = 0 # even position contor
        n = len(A)
        
        while i < n:
            if A[i] % 2 == 1: # odd number on even position
                
                # search for an even number on an odd position to swap
                while A[j] % 2 == 1:
                    j += 2
                
                # swap
                A[i], A[j] = A[j], A[i]
                
            i += 2
                
        return A

# Time: O(n)
# Space: O(1)