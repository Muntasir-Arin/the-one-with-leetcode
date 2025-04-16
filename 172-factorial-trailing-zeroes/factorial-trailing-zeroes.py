class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        while n>=5:
            num += n//5
            n/=5
        return int(num)