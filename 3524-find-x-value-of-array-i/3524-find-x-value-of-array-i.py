class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0]*k
        dp = [0]*k

        for num in nums:
            newdp = [0]*k
            x = num%k
            newdp[x] = 1

            for r in range(k):
                newr = (r*x)%k
                newdp[newr] += dp[r]

            for r in range(k):
                ans[r] += newdp[r] 
            
            dp = newdp

        return ans