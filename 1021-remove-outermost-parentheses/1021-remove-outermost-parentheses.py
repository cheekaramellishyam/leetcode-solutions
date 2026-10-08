class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        count = 0

        for ch in s:
            if ch == "(":
                if count > 0:
                    res += ch
                count += 1

            else:
                count -= 1
                if count > 0:
                    res += ch
        return res