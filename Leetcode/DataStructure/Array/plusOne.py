# 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ds = ""
        for digit in digits:
            ds += str(digit)
        
        re = int(ds) + 1
        re = str(re)

        result = []
        for r in re:
            result.append(int(r))
        return result
    
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits), -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits 
        return [1] + digits