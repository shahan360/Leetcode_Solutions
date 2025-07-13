class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1: Using Binary Search
        # if not matrix or not matrix[0]:
        #     return False
        # rows, cols = len(matrix), len(matrix[0])
        # left, right = 0, rows * cols - 1
        # while left <= right:
        #     mid  = left + (right - left) // 2
        #     mid_value = matrix[mid // cols][mid % cols]
        #     if mid_value == target:
        #         return True
        #     elif mid_value < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False

        # Approach 2: Start from the bottom-left corner, if the current number is less than the target, move up, if it's greater, move right
        # if not matrix or not matrix[0]:
        #     return False
        # rows, cols = len(matrix), len(matrix[0])
        # row, col = rows - 1, 0
        # while row >= 0 and col < cols:
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         col += 1
        #     else:
        #         row -= 1
        # return False

        # Approach 3: Two-pointer technique
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols - 1
        while left < rows and right >= 0:
            if matrix[left][right] == target:
                return True
            elif matrix[left][right] < target:
                left += 1
            else:
                right -= 1
        return False