class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        result = 0
        
        # Finding the common prefix
        while left < right:
            # Right-shift both left and right until they become equal
            left >>= 1
            right >>= 1
            
            # Increment the count of right shifts
            result += 1
        
        # Shift the common prefix back to obtain the final result
        return left << result