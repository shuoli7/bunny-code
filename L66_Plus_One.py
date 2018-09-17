class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        
        for i in reversed(range(1, len(digits))):
            if digits[i] != 10:
                break
            else:
                digits[i - 1] += 1
                digits[i] = 0
            
        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)
        return digits