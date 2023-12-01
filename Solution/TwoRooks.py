def solution(A):
  """Finds the maximum sum of two non-attacking rooks on a chessboard.

  Args:
    A: A 2D list representing the chessboard, where each element is an integer
        representing the points-based score of that square.

  Returns:
    The maximum sum of two non-attacking rooks on the chessboard.
  """

  # Get the number of rows and columns in the board
  N = len(A)
  M = len(A[0])

  # Initialize two lists to store the top 2 values in each row and column
  # For each row, we store the column indices of the top 2 values
  # For each column, we store the row indices of the top 2 values
  row = [[(0, -1), (0, -1)] for _ in range(N)]
  col = [[(0, -1), (0, -1)] for _ in range(M)]

  # For each row, find the top 2 values and remember the column where they were found
  for i in range(N):
    for j in range(M):
      if A[i][j] >= row[i][0][0]:
        row[i][1] = row[i][0]
        row[i][0] = (A[i][j], j)
      elif A[i][j] >= row[i][1][0]:
        row[i][1] = (A[i][j], j)

  # For each column, find the top 2 values and remember the row where they were found
  for j in range(M):
    for i in range(N):
      if A[i][j] >= col[j][0][0]:
        col[j][1] = col[j][0]
        col[j][0] = (A[i][j], i)
      elif A[i][j] >= col[j][1][0]:
        col[j][1] = (A[i][j], i)

  # Initialize a variable to store the maximum sum
  maxTwoRooks = 0

  # For each cell in the matrix, calculate the maximum sum that can be achieved by placing a rook on that cell
  for i in range(N):
    for j in range(M):
      r, c = i, row[i][0][1]
      if j != c:
        if col[j][0][1] != r:
          maxTwoRooks = max(maxTwoRooks, A[r][c] + A[col[j][0][1]][j])
        else:
          maxTwoRooks = max(maxTwoRooks, A[r][c] + A[col[j][1][1]][j])

      c, r = j, col[j][0][1]
      if i != r:
        if row[i][0][1] != c:
          maxTwoRooks = max(maxTwoRooks, A[r][c] + A[i][row[i][0][1]])
        else:
          maxTwoRooks = max(maxTwoRooks, A[r][c] + A[i][row[i][1][1]])

  return maxTwoRooks

print(solution([[1, 4], [2, 3]]))  # Output: 6
print(solution([[15, 1, 5], [16, 3, 8], [2, 6, 4]]))  # Output: 23
print(solution([[12, 12], [12, 12], [0, 7]]))  # Output: 24
print(solution([[1, 2, 14], [8, 3, 15]]))  # Output: 22