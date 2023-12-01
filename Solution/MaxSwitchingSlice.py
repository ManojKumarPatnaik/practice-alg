def solution(A):
  """Finds the length of the longest switching slice in an array.

  Args:
    A: A list of integers.

  Returns:
    The length of the longest switching slice in A.
  """

  # Check if the array has at least 3 elements.
  if len(A) < 3:
    # If the array has less than 3 elements, then the longest switching slice
    # is the length of the array.
    return len(A)

  # Initialize the length of the longest switching slice.
  longestSlice = 2

  # Initialize the length of the current switching slice.
  currentSlice = 2

  # Iterate over the array, starting at index 2.
  for i in range(2, len(A)):
    # If the current element is equal to the element at index i - 2, then the
    # current switching slice is extended.
    if A[i] == A[i - 2]:
      currentSlice += 1
    # Otherwise, the current switching slice is ended.
    else:
      # Start a new switching slice.
      currentSlice = 2

    # Update the length of the longest switching slice with the length of the
    # current switching slice, since it may be the longest.
    longestSlice = max(longestSlice, currentSlice)

  # Return the length of the longest switching slice.
  return longestSlice

print(solution([3, 2, 3, 2, 3]))  # Output: 5
print(solution([7, 4, -2, 4, -2, -9]))  # Output: 4
print(solution([7, -5, -5, -5, 7, -1, 7]))  # Output: 3
print(solution([4]))  # Output: 1