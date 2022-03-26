class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums1 = 0
        ans = 0
        for num in nums:
            if num == 1:
                nums1 += 1
            else:
                nums1 = 0
            ans = max(nums1, ans)
        return ans
