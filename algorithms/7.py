class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        rev = 0
        while x != 0:
            last_digit = int(math.fmod(x, 10))
            if ((rev > INT_MAX // 10 or (rev == INT_MAX // 10 and last_digit > 7)) or
                    (int(rev < INT_MIN / 10) or (rev == INT_MIN // 10 and last_digit < -8))):
                return 0
            rev = rev * 10 + last_digit
            x = int(x / 10)

        return rev
