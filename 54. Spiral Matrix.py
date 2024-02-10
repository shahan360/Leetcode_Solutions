def spiralOrder(matrix):
    result = []

    while matrix:
        # Append the elements of the first row
        result += matrix.pop(0)

        # Append the elements of the last column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Append the elements of the last row in reverse order
        if matrix and matrix[0]:
            result += matrix.pop()[::-1]

        # Append the elements of the first column in reverse order
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result

# Driver code
if __name__ == "__main__":
    # Example usage
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = spiralOrder(matrix)
    print(f"Spiral Order: {result}")
