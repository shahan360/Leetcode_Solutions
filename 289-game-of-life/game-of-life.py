class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: # Check if the board is empty or has no columns
            return # Early exit if the board is empty
        
        rows, cols = len(board), len(board[0]) # Get the number of rows and columns in the board
        
        # First pass: update the states
        for r in range(rows): # Iterate through each row
            for c in range(cols): # Iterate through each column
                live_neighbors = 0 # Initialize the count of live neighbors for the current cell
                
                # Count live neighbors
                for dr in [-1, 0, 1]: # Iterate through the relative row indices of neighbors
                    for dc in [-1, 0, 1]: # Iterate through the relative column indices of neighbors
                        if (dr == 0 and dc == 0) or not (0 <= r + dr < rows and 0 <= c + dc < cols): # Skip the current cell and out-of-bounds neighbors
                            continue # Skip the current cell and out-of-bounds neighbors
                        if board[r + dr][c + dc] in [1, 2]: # Check if the neighbor is alive (1) or marked as live that will die (2)
                            live_neighbors += 1 # Increment the count of live neighbors if the neighbor is alive or marked as live that will die
                # Apply the rules of the Game of Life
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3): # If the cell is currently alive and has fewer than 2 or more than 3 live neighbors, it dies
                    board[r][c] = 2 # Mark as live cell that will die
                elif board[r][c] == 0 and live_neighbors == 3: # If the cell is currently dead and has exactly 3 live neighbors, it becomes alive
                    board[r][c] = 3 # Mark as dead cell that will become alive  
        
        # Second pass: finalize the states
        for r in range(rows): # Iterate through each row again
            for c in range(cols): # Iterate through each column again
                if board[r][c] == 2: # If the cell was marked as a live cell that will die
                    board[r][c] = 0 # Live cell that will die becomes dead
                elif board[r][c] == 3: # If the cell was marked as a dead cell that will become alive
                    board[r][c] = 1 # Dead cell that will become alive becomes alive
        