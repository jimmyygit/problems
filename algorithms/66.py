class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        leng = len(digits) - 1
        for i, digit in enumerate(digits[::-1]):
            val = digit + carry
            digits[leng - i] = val % 10
            carry = val // 10

        if carry > 0:
            digits = [carry, *digits]
        return digits
