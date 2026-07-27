class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            target = -nums[i]

            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue 

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res

                
