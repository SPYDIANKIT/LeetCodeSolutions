class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1_set = set(nums1)
        
        # Iterate over nums2 and check for common elements
        for num in nums2:
            if num in nums1_set:
                return num
        
        # If no common element found, return a sentinel value
        return -1
        #