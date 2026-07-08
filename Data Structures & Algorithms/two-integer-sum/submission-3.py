class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = []
        for i, num in enumerate(nums):
            L.append([num, i])
        L.sort()
        i = 0 
        j = len(nums) - 1
        while i < j:
            sum_ = L[i][0] + L[j][0]
            
            if sum_ > target:
                j -= 1
            elif sum_ < target:
                i += 1
            else:
                return [min(L[i][1], L[j][1]), max(L[i][1], L[j][1])]
        return []
            
            



