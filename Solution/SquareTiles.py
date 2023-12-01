def solution(M, N):
  """
  Given two integers M and N, returns the length of the side of the largest
  square you can create. If no square can be created, returns 0.

  Args:
    M: The number of 1x1 tiles.
    N: The number of 2x2 tiles.

  Returns:
    The length of the side of the largest square you can create.
  """

  # Calculate the total area of the tiles.
  totalArea = M + 4 * N

  # Initialize the side length of the square.
  side = int(totalArea**0.5)

  # If the side length is even, we can perfectly fill a square of this size with the tiles.
  if side % 2 == 0:
    return side
  else:
    # If the side length is odd, we compute the number of 2x2 squares that can fit in a square of size (side-1).
    inter = ((side - 1) * (side - 1)) // 4

    # We check if we have enough tiles to fill a square of size 'side'. If we do, we return 'side'.
    if 4 * min(inter, N) + M >= side * side:
      return side
    else:
      # If we don't have enough tiles to fill a square of size 'side', we return 'side - 1'.
      return side - 1

print(solution(8, 0))  # Output: 2
print(solution(4, 3))  # Output: 4
print(solution(0, 18))  # Output: 8
print(solution(13, 3))  # Output: 5
