from typing import List, Optional

def n_queen(n: int, first_queen: Optional[List[int]] = None) -> List[List[int]]:
    # Initialize the chessboard with zeros
    chessboard = [[0] * n for _ in range(n)]
    
    if first_queen is not None:
        # Place the first queen on the chessboard
        row, col = first_queen
        chessboard[row][col] = 1
    
    def is_valid(row, col):
        # Check if the current position is valid
        for i in range(row):
            if chessboard[i][col]:
                return False
            if col - (row - i) >= 0 and chessboard[i][col - (row - i)]:
                return False
            if col + (row - i) < n and chessboard[i][col + (row - i)]:
                return False
        return True
    
    def solve(row):
        # Recursive function to place queens on the chessboard
        if row == n:
            # All queens have been placed, return the chessboard
            return chessboard
        for col in range(n):
            if is_valid(row, col):
                chessboard[row][col] = 1
                if solve(row + 1):
                    return chessboard
                chessboard[row][col] = 0
        return None
    
    # Call the solve function to find the solution
    return solve(1 if first_queen is not None else 0)
