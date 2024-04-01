class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for _ in range(len(s)):
            s = s[-1] + s[:-1]  # Rotate the string
            if s == goal:
                return True
        return False
