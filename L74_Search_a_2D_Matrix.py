class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
            
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        while up <= down:
            if matrix[up][-1] >= target:
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[up][mid] == target:
                        return True
                    elif matrix[up][mid] < target:
                        left += 1
                    else:
                        right -= 1
            up += 1
        return False