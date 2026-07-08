class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ri in range(len(matrix)):
            l, r = 0, len(matrix[ri]) - 1
            while l<=r:
                mid = l + ((r-l) // 2)

                if matrix[ri][mid] > target:
                    r = mid - 1
                elif matrix[ri][mid] < target:
                    l = mid + 1
                else:
                    return True 
        return False