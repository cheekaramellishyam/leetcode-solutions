class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
     
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                    break
                last = stack.pop()
                if i == ")" and last!="(":
                    return False
                    break
                if i == "]" and last!="[":
                    return False
                    break
                if i == "}" and last!="{":
                    return False
                    break
        return len(stack) == 0     