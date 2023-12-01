def solution(S):
  """
  Given a string S of length N representing arrow keys pressed by each of the players, returns the number of players that will perform a move successfully.

  Args:
    S: A string of length N representing arrow keys pressed by each of the players.

  Returns:
    The number of players that will perform a move successfully.
  """

  N = len(S)
  moves = 0

  # Check if the previous player is moved
  isMoved = False

  # If the first player is trying to move left, the move is successful.
  if S[0] != ">":
    isMoved = True
    moves = 1

  for i in range(1, N):
    # If the current player is trying to move left and the previous player moved right,
    # or if the current player is trying to move left and the previous player is not moved,
    # or if the current player is trying to move right and player is not the last player,
    # the move is not successful.
    if (S[i - 1] == ">" and S[i] == "<") or (S[i] == "<" and not isMoved) or (S[i] == ">" and i < N - 1):
      isMoved = False
      continue
    # Otherwise, the move is successful.
    else:
      isMoved = True
      moves += 1

  return moves

print(solution("><^v"))  # Output: 2
print(solution("<<^<v>>"))  # Output: 6
print(solution("><><"))  # Output: 0
