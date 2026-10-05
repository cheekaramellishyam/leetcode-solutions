class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                inside = stack.pop()
                if inside == 0:
                    score = 1
                else:
                    score = 2*inside
                stack[-1] = score + stack[-1]
        return stack[0]