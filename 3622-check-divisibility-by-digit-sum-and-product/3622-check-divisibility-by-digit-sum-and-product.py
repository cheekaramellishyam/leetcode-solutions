class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = sum(int(digit) for digit in str(n))
        p = 1
        for digit in str(n):
            p *= int(digit)
        if n%(s+p)==0:
            return True
        else:
            return False
        