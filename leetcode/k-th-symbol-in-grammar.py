class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def worker( row,k):
            if row == 1:
                return 0
            center=2**(row-2)
            if k <=center:  # Check if k belongs to the first half
                return worker(row - 1,k)
            else:
                return 1- worker(row - 1,k-center)  # Flip the current value for the second half
        return worker(n, k)  # Adjust k to zero-based indexing

    

