class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # We are given a number of rows, we need to generate the pascal triangle for that many rows
        triangle = []
        for i in range(numRows):
            # For each row, we need to create a new list
            row = [1] * (i + 1)
            '''
            Visualization of above line:
            For i = 0: row = [1]
            For i = 1: row = [1, 1]
            For i = 2: row = [1, 1, 1]
            For i = 3: row = [1, 1, 1, 1]
            For i = 4: row = [1, 1, 1, 1, 1]
            '''
            # For the first and last element of each row, we need to set it to 1
            for j in range(1, i):
                # For each element in the row, we need to set it to the sum of the two elements above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            '''
            Visualization of above loop:
            For i = 1: row = [1, 1] (no change)
            For i = 2: row = [1, 2, 1] (1 + 1 = 2)
            For i = 3: row = [1, 3, 3, 1] (1 + 2 = 3 and 2 + 1 = 3)
            For i = 4: row = [1, 4, 6, 4, 1] (1 + 3 = 4, 3 + 3 = 6, and 3 + 1 = 4)
            '''
            # We need to append the row to the triangle
            triangle.append(row)
            ''' Visualization of triangle after each row:
            After i = 0: triangle = [[1]]
            After i = 1: triangle = [[1], [1, 1]]
            After i = 2: triangle = [[1], [1, 1], [1, 2, 1]]
            After i = 3: triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
            After i = 4: triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
            '''
        return triangle