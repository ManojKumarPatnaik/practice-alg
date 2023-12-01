def solution(A):
  """
  Finds the minimum possible maximum difference between the largest and smallest integer in each of three non-empty groups of the given array.

  Args:
    A: A list of integers.

  Returns:
    The minimum possible maximum difference.
  """

  # Sort the array in ascending order.
  A.sort()

  # Initialize the minimum and maximum possible maximum differences.
  minDiff = 0
  maxDiff = A[-1] - A[0]

  # Iterate over the middle of the range of possible maximum differences.
  while minDiff < maxDiff:
    # Calculate the middle possible maximum difference.
    midDiff = (minDiff + maxDiff) // 2

    # Initialize the number of groups and the minimum and maximum values in the current group.
    number_groups = 1
    minGroup = maxGroup = A[0]

    # Iterate over the array and try to form three non-empty groups with the current middle possible maximum difference.
    for i in range(1, len(A)):
      # Update the minimum and maximum values in the current group.
      minGroup = min(minGroup, A[i])
      maxGroup = max(maxGroup, A[i])

      # If the maximum difference in the current group is greater than the middle possible maximum difference,
      # then we need to form a new group.
      if maxGroup - minGroup > midDiff:
        number_groups += 1
        minGroup = maxGroup = A[i]

    # If we need to form more than three groups with the current middle possible maximum difference,
    # then the minimum possible maximum difference is greater than the middle possible maximum difference.
    if number_groups > 3:
      minDiff = midDiff + 1
    # Otherwise, the maximum possible maximum difference is less than or equal to the middle possible maximum difference.
    else:
      maxDiff = midDiff

  # Return the minimum possible maximum difference.
  return maxDiff

print(solution([11, 5, 3, 12, 6, 8, 1, 7, 4]))  # Output: 3
print(solution([10, 14, 12, 1000, 11, 15, 13, 1]))  # Output: 5
print(solution([4, 5, 7, 10, 10, 12, 12, 12]))  # Output: 2
print(solution([5, 10, 10, 5, 5]))  # Output: 0