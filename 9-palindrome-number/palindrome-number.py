class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        y=x
        while y:
            rev = rev * 10 + y % 10
            y //= 10
        return rev == x
        