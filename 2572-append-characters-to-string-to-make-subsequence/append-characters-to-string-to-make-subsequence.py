class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_ptr, t_ptr = 0, 0
        s_len, t_len = len(s), len(t)
        
        # Traverse both strings
        while s_ptr < s_len and t_ptr < t_len:
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1
        
        # If t_ptr is equal to the length of t, it means t is already a subsequence of s
        if t_ptr == t_len:
            return 0
        
        # Return the remaining characters in t that need to be appended
        return t_len - t_ptr
