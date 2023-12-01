def isAssassinStealth(x, y, reworkB):
  # Number of rows in the board
  N = len(reworkB)
  # Number of columns in the board
  M = len(reworkB[0])

  if x == N - 1 and y == M - 1:
    return True

  if (N - 1 < x or x < 0) or (M - 1 < y or y < 0) or reworkB[x][y] == "X":
    return False
  else:
    reworkB[x][y] = "X"
  
  return isAssassinStealth(x - 1, y, reworkB) or isAssassinStealth(x + 1, y, reworkB) or isAssassinStealth(x, y - 1, reworkB) or isAssassinStealth(x, y + 1, reworkB)

def solution(B):
  """
  Determines whether the assassin can move stealthily to the bottom-right cell of the board
  without being detected by guards.

  Args:
    B: A two-dimensional array representing the board, where each element is a character
        representing either an empty cell ('.'), an obstacle ('X'), a guard ('<', '>', '^', or 'v'),
        or the assassin ('A')

  Returns:
    True if the assassin can reach the bottom-right cell undetected, and False otherwise.
  """

  # Number of rows in the board
  N = len(B)
  # Number of columns in the board
  M = len(B[0])
  # Create a copy of the board to mark explored positions
  reworkB = [["." for j in range(M)] for i in range(N)]

  # Initialize the starting position of the assassin
  x = 0
  y = 0
  # Scan the board to identify guards and their directions
  for i in range(N):
    for j in range(M):
      # Guard facing right
      if B[i][j] == ">":
        # Check the guard's line of sight to the right
        for k in range(j + 1, M):
          # If the assassin is in the guard's line of sight, return False
          if B[i][k] == "A":
            return False
          # Mark explored positions in the guard's line of sight
          elif B[i][k] == ".":
            reworkB[i][k] = "X"
          # Obstacle encountered, stop checking the line of sight
          else:
            break
        # Mark the guard's position as explored
        reworkB[i][j] = "X"
      # Guard facing left
      elif B[i][j] == "<":
        # Check the guard's line of sight to the left
        for k in range(j - 1, -1, -1):
          # If the assassin is in the guard's line of sight, return False
          if B[i][k] == "A":
            return False
          # Mark explored positions in the guard's line of sight
          elif B[i][k] == ".":
            reworkB[i][k] = "X"
          # Obstacle encountered, stop checking the line of sight
          else:
            break
        # Mark the guard's position as explored
        reworkB[i][j] = "X"
      # Guard facing down
      elif B[i][j] == "v":
        # Check the guard's line of sight downwards
        for k in range(i + 1, N):
          # If the assassin is in the guard's line of sight, return False
          if B[k][j] == "A":
            return False
          # Mark explored positions in the guard's line of sight
          elif B[k][j] == ".":
            reworkB[k][j] = "X"
          # Obstacle encountered, stop checking the line of sight
          else:
            break
        # Mark the guard's position as explored
        reworkB[i][j] = "X"
      # Guard facing upwards
      elif B[i][j] == "^":
        # Check the guard's line of sight upwards
        for k in range(i - 1, -1, -1):
          # If the assassin is in the guard's line of sight, return False
          if B[k][j] == "A":
            return False
          # Mark explored positions in the guard's line of sight
          elif B[k][j] == ".":
            reworkB[k][j] = "X"
          # Obstacle encountered, stop checking the line of sight
          else:
            break
        # Mark the guard's position as explored
        reworkB[i][j] = "X"
      # Mark obstacles as explored
      elif B[i][j] == "X":
        reworkB[i][j] = "X"
      # Identify the assassin's starting position
      elif B[i][j] == "A":
        # Mark the assassin's starting position as explored
        x = i
        y = j
        reworkB[i][j] = "A"
      # Ignore empty cells
      else:
        continue

  # Check if the bottom-right cell is marked as explored, indicating a clear path for the assassin
  if reworkB[N - 1][M - 1] == "X":
    return False

  # Using DFS to check if Assassin can stealth
  return isAssassinStealth(x, y, reworkB)

print(solution(["X.....>", "..v..X.", ".>..X..", "A......"]))  # Output: False
print(solution(["...Xv", "AX..^", ".XX.."]))  # Output: True
print(solution(["...", ">.A"]))  # Output: False
print(solution(["A.v", "..."]))  # Output: False