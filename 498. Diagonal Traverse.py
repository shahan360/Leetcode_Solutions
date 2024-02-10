def findDiagonalOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    for i in range(rows + cols - 1):
        if i % 2 == 0:  # Upward diagonal
            for j in range(min(i, rows - 1), max(0, i - cols + 1) - 1, -1):
                result.append(matrix[j][i - j])
        else:  # Downward diagonal
            for j in range(min(i, cols - 1), max(0, i - rows + 1) - 1, -1):
                result.append(matrix[i - j][j])

    return result

# Driver code
if __name__ == "__main__":
    # Example usage
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = findDiagonalOrder(matrix)
    print(f"Diagonal Traverse: {result}")
