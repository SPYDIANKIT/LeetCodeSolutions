class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
         # Split the string into words
        words = s.split()

        # Check if there are any words
        if not words:
            return 0

        # Return the length of the last word
        return len(words[-1])