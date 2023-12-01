def checkBattleShip(i, j, B, unidentifiedShip):
  """Recursively checks if the cell at (i, j) is part of a battleship.

  Args:
    i: The row index of the cell.
    j: The column index of the cell.
    B: The game board.
    unidentifiedShip: A list of the cells that are part of the battleship.

  Returns:
    None.
  """

  # If the battleship already has 3 cells, return.
  if len(unidentifiedShip) == 3:
    return

  N = len(B)
  M = len(B[0])

  # Check the four adjacent cells.
  for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    # If the new cell is within the bounds of the board and has not been
    # visited yet, and is a part of the ship, add it to the list of
    # unidentified cells and recursively check its neighbors.
    if (0 <= i + dx < N) and (0 <= j + dy < M):
      if B[i + dx][j + dy] == "#" and (i + dx, j + dy) not in unidentifiedShip:
        unidentifiedShip.append((i + dx, j + dy))
        checkBattleShip(i + dx, j + dy, B, unidentifiedShip)

def solution(B):
  """Finds the number of ships of each type on a Battleships board.

  Args:
    B: A list of strings, where each string represents a row of the game board.

  Returns:
    A list of three integers, where the first integer represents the number of
    Patrol Boats, the second integer represents the number of Submarines, and
    the third integer represents the number of Destroyers.
  """

  N = len(B)
  M = len(B[0])

  patrols = []
  submarines = []
  destroyers = []

  # Iterate over the rows of the board.
  for i in range(N):
    # Iterate over the columns of the board.
    for j in range(M):
      unidentifiedShip = []

      # If the cell is part of a ship and has not been visited yet,
      # start recursively checking its neighbors to find the size of the ship.
      if B[i][j] == "#" and (i, j) not in patrols and (i, j) not in submarines and (i, j) not in destroyers:
        unidentifiedShip.append((i, j))
        checkBattleShip(i, j, B, unidentifiedShip)

      # Add the ship to the appropriate list, depending on its size.
      if len(unidentifiedShip) == 3:
        destroyers.extend(unidentifiedShip)
      elif len(unidentifiedShip) == 2:
        submarines.extend(unidentifiedShip)
      else:
        patrols.extend(unidentifiedShip)

  # Return the number of ships of each type.
  return [len(patrols) // 1, len(submarines) // 2, len(destroyers) // 3]

print(solution([".##.#", "#.#..", "#...#", "#.##."]))  # Output: [2, 1, 2]
print(solution([".#..#", "##..#", "...#."]))  # Output: [1, 1, 1]
print(solution(["##.", "#.#", ".##"]))  # Output: [0, 0, 2]
print(solution(["...", "...", "..."]))  # Output: [0, 0, 0]