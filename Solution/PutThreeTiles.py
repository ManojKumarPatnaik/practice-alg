def solution(A):
  """
  Finds the maximum sum of numbers that can be covered using at most three tiles in a given array of integers.

  Args:
    A (list[int]): An array of N integers

  Returns:
    int: The maximum sum of numbers that can be covered using at most three tiles
  """

  # Get the length of the array
  N = len(A)

  # Initialize the list for the maximum sum of one tile
  maxOneTile = [0] * N
  # Initialize the list for the maximum sum of two tiles
  maxTwoTile = [0] * N
  # Initialize the list for the maximum sum of three tiles
  maxThreeTile = [0] * N
  # Calculate the maximum sum for the first few elements
  maxOneTile[1] = A[0] + A[1]
  for i in range(2, N):
    maxOneTile[i] = max(maxOneTile[i-1], A[i-1] + A[i])
    if i > 2:
      # Calculate the maximum sum that can be covered by two tiles at each position
      maxTwoTile[i] = max(maxTwoTile[i-1], maxOneTile[i-2] + A[i-1] + A[i])
    if i > 4:
      # Calculate the maximum sum that can be covered by three tiles at each position
      maxThreeTile[i] = max(maxThreeTile[i-1], maxTwoTile[i-2] + A[i-1] + A[i])
  # Return the maximum sum that can be covered by at most three tiles
  return max(maxOneTile[-1], maxTwoTile[-1], maxThreeTile[-1])

print(solution([2, 3, 5, 2, 3, 4, 6, 4, 1]))  # Output: 25
print(solution([1, 5, 3, 2, 6, 6, 10, 4, 7, 2, 1]))  # Output: 35
print(solution([1, 2, 3, 3, 2]))  # Output: 10
print(solution([5, 10, 3]))  # Output: 15
