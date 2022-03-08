class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        if (needle_len == 0):
            return 0
        window = haystack[0:needle_len]
        if window == needle:
            return 0
        for i in range(needle_len, len(haystack)):
            window = window[1:] + haystack[i]
            if window == needle:
                return i - needle_len + 1
        return -1
