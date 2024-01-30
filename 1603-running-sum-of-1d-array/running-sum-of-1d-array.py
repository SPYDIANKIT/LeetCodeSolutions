class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=[]
        
        for a in range(len(nums)):
            curr_sum = 0
            for b in range(a + 1):
                curr_sum += nums[b]
            sum.append(curr_sum)
        return sum