class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        intersection = []
        
        # Iterate over nums2 and check for common elements
        for num in nums2:
            if num in nums1_set:
                intersection.append(num)
        intersection = list(set(intersection))
        
        return intersection