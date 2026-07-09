class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxTrapped = 0
        max_ = 0
        while l<r:
            if height[l] < height[r]:
                max_ = max(height[l], max_)
                maxTrapped += (max_ - height[l])
                l+=1
            else:
                max_ = max(height[r], max_)
                maxTrapped += (max_ - height[r])
                r -= 1
        return maxTrapped



