def solution(A):
  """Finds the maximum number of non-intersecting segments of length 2
  (two adjacent elements), such that segments have an equal sum.

  Args:
    A: A list of integers.

  Returns:
    The maximum number of non-intersecting segments of length 2 with equal sums.
  """

  # Get the length of the input array.
  N = len(A)

  # Initialize the maximum number of segments.
  maxSegments = 1

  # Iterate over the input array, starting from index 1.
  for i in range(1, N):
    # Calculate the sum of the current and previous elements.
    equalSum = A[i - 1] + A[i]

    # Initialize the number of segments with the current sum.
    currentSegments = 1

    # Iterate over the remaining elements in the array.
    j = i + 1
    while j < N - 1:
      # If the sum of the current and next elements is equal to the current sum,
      # then increment the number of segments with the current sum.
      if equalSum == A[j] + A[j + 1]:
        currentSegments += 1
        j += 2  # Skip the next two elements.
      # Otherwise, move on to the next element.
      else:
        j += 1

    # Update the maximum number of segments with the current sum.
    maxSegments = max(maxSegments, currentSegments)

  # Return the maximum number of segments.
  return maxSegments

print(solution([10, 1, 3, 1, 2, 2, 1, 0, 4]))  # Output: 3
print(solution([5, 3, 1, 3, 2, 3]))  # Output: 1
print(solution([9, 9, 9, 9, 9]))  # Output: 2
print(solution([1, 5, 2, 4, 3, 3]))  # Output: 3
