class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        result = []
        
        # Append characters from order, preserving their order
        for char in order:
            if char in char_count:
                result.append(char * char_count[char])
                del char_count[char]
        
        # Append remaining characters in s (not in order) to the result
        for char in char_count:
            result.append(char * char_count[char])
        
        return ''.join(result)