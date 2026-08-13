class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1 # cus we are adding 1 
        i = len(digits) - 1
        
        while i >= 0:
            # 19 + 1 and 199 + 1 
            digits[i] += carry 
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
            i -= 1
        # 9 + 1
        if carry:
            return [1] + digits
        return digits

# you can do it reversed as well