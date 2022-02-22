class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        ind = 0
        end = False
        while not end:
            for s in strs:
                if ind == len(s):
                    end = True
                    break
            if end:
                break

            letter = s[ind]
            for s in strs:
                if s[ind] != letter:
                    end = True
                    break
            if not end:
                ans += letter
                ind += 1

        return ans
