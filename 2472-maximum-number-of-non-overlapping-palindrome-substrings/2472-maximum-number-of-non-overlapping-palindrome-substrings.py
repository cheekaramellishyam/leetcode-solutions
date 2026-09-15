class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for length in (k, k+1):
                start = i - length
                if start >= 0:
                    sub = s[start:i]
                    if sub == sub[::-1]:
                        dp[i] = max(dp[i], dp[start] + 1)
        
        return dp[n]
