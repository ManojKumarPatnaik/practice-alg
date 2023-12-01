def solution(blocks):
  """
  Calculates the maximum possible distance between two frogs sitting on blocks.

  Args:
    blocks (list): A list of integers representing the heights of the blocks.

  Returns:
    int: The maximum possible distance between the two frogs.
  """

  # Get the number of blocks
  N = len(blocks)

  # Initialize the longest distance found so far
  longestDistance = 0

  # Iterate through the blocks array
  for i in range(N):
    # Initialize the left and right distances
    leftDistance = i
    rightDistance = i

    # Move the left pointer to the left while the block height is non-decreasing
    while leftDistance > 0 and blocks[leftDistance - 1] >= blocks[leftDistance]:
      leftDistance -= 1

    # Move the right pointer to the right while the block height is non-decreasing
    while rightDistance < N - 1 and blocks[rightDistance + 1] >= blocks[rightDistance]:
      rightDistance += 1

    # Update the longest distance if necessary
    longestDistance = max(longestDistance, rightDistance - leftDistance + 1)

  # Return the longest distance found
  return longestDistance

print(solution([2, 6, 8, 5]))  # Output: 3
print(solution([1, 5, 5, 2, 6]))  # Output: 4
print(solution([1, 1]))  # Output: 2
