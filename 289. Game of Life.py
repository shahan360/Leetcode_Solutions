def gameOfLife(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    # Helper function to count live neighbors
    def countLiveNeighbors(x, y):
        live_neighbors = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (board[nx][ny] == 1 or board[nx][ny] == -1):
                live_neighbors += 1

        return live_neighbors

    # Iterate through each cell in the board
    for i in range(rows):
        for j in range(cols):
            live_neighbors = countLiveNeighbors(i, j)

            # Apply the rules of the Game of Life
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = -1  # Mark as dying
            else:
                if live_neighbors == 3:
                    board[i][j] = 2  # Mark as coming to life

    # Update the board based on the marked cells
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1

# Driver code
if __name__ == "__main__":
    # Example usage
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    gameOfLife(board)
    print(f"Updated Game of Life Board: {board}")
