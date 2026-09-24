class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, val in enumerate(nums):
            dig_sum = sum(int(digit) for digit in str(val))
            if dig_sum == i:
                return i

        return -1    

        