class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= postfix 
            postfix *= nums[j]

        return output