class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powHelper(x, n):
            if n == 0:
                return 1
            half = powHelper(x, n // 2)
            result = half * half
            if n % 2 == 1:
                result *= x
            return result
        
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        return powHelper(x, N)