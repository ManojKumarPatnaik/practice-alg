def solution(A):
  """
  This function determines the minimum number of filters required to reduce the total pollution emitted by a list of factories by at least half.
  Args:
      A (list): A list of integers representing the pollution emitted by each factory.
  Returns:
      int: The minimum number of filters required to reduce the total pollution by at least half.
  """

  # Get the number of factories
  N = len(A)
  # Calculate the total pollution emitted by all factories
  total = sum(A)
  # Set the target pollution level (half of the original total)
  target = total / 2
  # Initialize the counter for the number of filters used
  filters = 0

  # Continue iterating until the total pollution is less than or equal to the target
  while total > target:
    # Update the maximum pollution value
    maxPollution = max(A)
    # Update the index of the factory with the maximum pollution
    checkPoint = A.index(maxPollution)
    # Reduce the pollution of the factory with the maximum pollution by half
    A[checkPoint] = A[checkPoint] / 2
    # Update the total pollution
    total = total - (maxPollution / 2)
    # Increment the counter for the number of filters used
    filters += 1

  return filters

print(solution([5, 19, 8, 1]))  # Output: 3
print(solution([10, 10]))  # Output: 2
print(solution([3, 0, 5]))  # Output: 2