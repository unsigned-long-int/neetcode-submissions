class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stacked = []
        maxArea = 0
        for i in range(len(heights)):
            index = i
            while stacked and heights[i] < stacked[-1][1]:
                index, height = stacked.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)

            stacked.append([index, heights[i]])
        maxArea = max(maxArea, max(stacked[i][1] * (len(heights)- stacked[i][0]) for i in range(len(stacked))))
        return maxArea


