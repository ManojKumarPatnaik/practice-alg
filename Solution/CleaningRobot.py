def solution(R):
  """
  Calculates the number of clean squares covered by the robot.

  Args:
    R: An array of strings representing the grid.

  Returns:
    The number of clean squares.
  """

  # Get the dimensions of the grid
  N = len(R)
  M = len(R[0])

  # Define the possible movement directions
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  # Initialize the starting position and direction
  i = 0
  j = 0
  clockwise = 0

  # Track the cleaning path using a dictionary
  cleaningPath = {(0, 0): 1}

  # Explore the grid until the robot revisits a position
  while True:
    # Get the current direction vector
    dx, dy = directions[clockwise]

    # Check if the next position is valid and empty
    if -1 < i + dx < N and -1 < j + dy < M and R[i + dx][j + dy] == ".":

      # Update the cleaning path count for the next position
      cleaningPath[(i + dx, j + dy)] = cleaningPath.get((i + dx, j + dy), 0) + 1

      # Check if the next position has been visited more than twice
      if cleaningPath[(i + dx, j + dy)] > 2:
        # If so, the robot has revisited a position, so stop exploring
        break

      # Update the robot's position
      i += dx
      j += dy

    # If the next position is invalid or occupied
    else:
      # Rotate the robot clockwise
      clockwise = clockwise + 1 if clockwise < 3 else 0

      # Check if the robot has reached the starting position and no cleaning has been done
      if clockwise == 0 and len(cleaningPath) == 1:
        # If so, the robot has not explored any new positions, so stop exploring
        break

  # Return the number of unique positions cleaned by the robot
  return len(cleaningPath)

print(solution(["...X..", "....XX", "..X..."]))  # Output: 6
print(solution(["....X..", "X......", ".....X.", "......."]))  # Output: 15
print(solution(["...X.", ".X..X", "X...X", "..X.."]))  # Output: 9
print(solution(["."]))  # Output: 1
