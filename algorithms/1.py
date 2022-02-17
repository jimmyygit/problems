class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            if num in complements.keys():
                return [complements[num], i]
            else:
                complements[target - num] = i
