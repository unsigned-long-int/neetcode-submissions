class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1

        return res