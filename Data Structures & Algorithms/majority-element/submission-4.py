class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hMap = {}
        for item in nums:
            hMap[item] = hMap.get(item, 0) + 1

        max_ = 0
        par = 0
        for k, v in hMap.items():
            if v > max_:
                max_ = v 
                par = k

        return par