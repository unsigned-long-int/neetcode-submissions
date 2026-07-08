class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hMap = {}
        for item in nums:
            hMap[item] = hMap.get(item, 0) + 1
            if hMap[item] > (len(nums) / 2):
                return item