def solution(A):
  """
  Finds the largest sum of a subarray whose first and last elements have the same value.
  If there is no such subarray, returns -1.

  Args:
    A (list): An array of N positive integers.

  Returns:
    int: The largest sum of a subarray whose first and last elements have the same value, or -1 if no such subarray exists.
  """

  # Get the length of the array
  N = len(A)

  # Create a dictionary to store the indices of each element's first and last occurrences
  numbersIndex = {}
  for i in range(N):
    # If the element is not in the dictionary, add it
    if A[i] not in numbersIndex:
      # Initialize the first and last occurrences to the current index
      numbersIndex[A[i]] = [i, i] 
    else:
      # Update the last occurrence index
      numbersIndex[A[i]][1] = i

  # Initialize the maximum subarray sum to -1
  maxSubArray = -1
  # Iterate through the dictionary of element occurrences
  for _, (minIndex, maxIndex) in numbersIndex.items():
    # Check if there is at least one occurrence before the current one
    if minIndex != maxIndex:
      # Calculate the sum of the subarray
      currentSum = sum(A[minIndex:maxIndex + 1])
      # Update the maximum subarray sum
      maxSubArray = max(maxSubArray, currentSum)

  return maxSubArray

print(solution([1, 3, 6, 1, 6, 6, 9, 9]))  # Output: 19
print(solution([5, 1, 4, 3]))  # Output: -1
print(solution([2, 2, 2, 3, 2, 3]))  # Output: 11