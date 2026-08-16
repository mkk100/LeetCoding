# come back to itclass Solution(object):
def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        res, i, carry = "", 0, 0
        def addBin(total, carry, res):
            if total == 0:
                res += "0"
            elif total == 1:
                res += "1"
                carry = 0
            elif total == 2:
                res += "0"
                carry = 1
            elif total == 3:
                res += "1"
                carry = 1
            return carry, res
        
        while i < len(a) and i < len(b):
            total = int(a[i]) + int(b[i]) + carry
            carry, res = addBin(total, carry, res)
            i += 1

        while i < len(a):
            total = int(a[i]) + carry
            carry, res = addBin(total, carry, res)
            i += 1
        
        while i < len(b):
            total = int(b[i]) + carry
            carry, res = addBin(total, carry, res)
            i += 1

        if carry:
            res += "1"

        return res[::-1]
# not optimal nor that clean

# for loop len(max) allows you to not do two more loops
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        res, i, carry = "", 0, 0

        def addBin(total,carry,res):
            res += str(total % 2)
            carry = total // 2
            return res, carry
        for i in range(max(len(a), len(b))): 
            total = (
                (int(a[i]) if i < len(a) else 0)
                + (int(b[i]) if i < len(b) else 0)
                + carry
            )
            res, carry = addBin(total, carry, res)
            i += 1
        if carry:
            res += "1"

        return res[::-1]

            