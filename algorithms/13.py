class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        ans = 0
        i = 0
        while i < len(s):
            key = s[i]
            if (i < len(s) - 1):
                if ((s[i] == 'I' and s[i+1] in ['V', 'X']) or
                   (s[i] == 'X' and s[i+1] in ['L', 'C']) or
                   (s[i] == 'C' and s[i+1] in ['D', 'M'])):
                    key += s[i+1]
                    i += 1
            print(key)
            ans += roman[key]
            i += 1
        return ans
