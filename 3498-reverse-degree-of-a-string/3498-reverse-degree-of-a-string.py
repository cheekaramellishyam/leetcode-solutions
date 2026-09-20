class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            degree = ord('z') - ord(s[i])+1
            ans += degree*(i+1)
        return ans