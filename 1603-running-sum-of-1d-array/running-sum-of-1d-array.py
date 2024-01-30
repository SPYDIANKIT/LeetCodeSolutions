class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            result.append(curr_sum)
        return result