class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j=len(a)-1,len(b)-1
        result=''
        carry=0

        while i>=0 or j>=0:
             # Extract the current bits from both strings
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of the bits and the carry
            total = bit_a + bit_b + carry
            
            # Determine the current bit of the result
            result = str(total % 2) + result
            
            # Update the carry
            carry = total // 2
            
            # Move to the next bits towards left
            i -= 1
            j -= 1
        
        # If there's still a carry after all bits are exhausted, add it to the result
        if carry:
            result = '1' + result
        
        return result