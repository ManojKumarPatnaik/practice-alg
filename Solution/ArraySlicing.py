def solution(A):
  """Returns the maximum number of slices for which the algorithm will return a correctly sorted array.

  Args:
    A: A list of distinct integers.

  Returns:
    An integer representing the maximum number of slices.
  """

  # Get the length of the array
  N = len(A)

  # Initialize an array to store the minimum value from the right side of the array for each index
  minFromRight = [None] * N
  minFromRight[N - 1] = A[N - 1]  # Set the last element as the minimum from the right

  # Iterate from the second-to-last element to the beginning of the array
  for i in range(N - 2, -1, -1):
    minFromRight[i] = min(minFromRight[i + 1], A[i])  # Update the minimum value for each index

  # Initialize variables to track the number of slices and the maximum value encountered so far
  slices = 1
  maxSlice = 0

  # Iterate from the beginning of the array to the second-to-last element
  for i in range(N - 1):
      maxSlice = max(maxSlice, A[i])  # Update the maximum value encountered so far
      # Check if the maximum value is less than or equal to the minimum value from the right side
      if maxSlice <= minFromRight[i + 1]:
          slices += 1  # Increment the number of slices if a slice boundary is found

  # Return the maximum number of slices
  return slices

print(solution([2, 4, 1, 6, 5, 9, 7]))  # Ouput: 3
print(solution([4, 3, 2, 6, 1]))  # Ouput: 1
print(solution([2, 1, 6, 4, 3, 7]))  # Ouput: 3