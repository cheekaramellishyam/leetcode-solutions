class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_strs = float("inf")
        i = 0
        for s in strs:
            if len(s) < min_strs:
                min_strs = len(s)

        while i < min_strs:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]

            i += 1
        return strs[0][:min_strs]
        