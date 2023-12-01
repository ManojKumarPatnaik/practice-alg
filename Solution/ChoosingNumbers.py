def solution(A):
  """
  Find the maximum length of a consecutive sequence of elements in the given array A
  such that the differences between all pairs of consecutive integers are equal.

  Args:
    A (list): An array of integers

  Returns:
    int: The maximum length of a consecutive sequence
  """

  # Create a dictionary to store the count of occurrences for each distinct element
  numberCounts = {number: A.count(number) for number in A}
  # Find the maximum duplicate count
  maxLength = max(numberCounts.values())

  # Convert A to a sorted set to remove duplicates and order to ascending
  A = sorted(set(A))
  # Get the length of the unique elements
  N = len(A)

  # Check for edge cases where N is less than 3
  if N < 3:
    # Return the maximum of maxLength and N
    return 2

  # Nested loop to iterate through possible pairs of consecutive elements (i, j) in A
  for i in range(N - 1):
    for j in range(i + 1, N):
      currentLength = 2
      # Calculate the difference between the current and next elements
      diff = A[j] - A[i]
      # Calculate the possible next number
      nextNumber = A[j] + diff
      # While loop to extend the consecutive sequence as long as possible
      while numberCounts.get(nextNumber, 0) != 0:
        currentLength += 1
        nextNumber = diff + nextNumber
      # Compare the length of the current sequence to the maximum length
      maxLength = max(maxLength, currentLength)
  # Return the maximum length of the consecutive sequence
  return maxLength

print(solution([4, 3, 5, 1, 4, 4]))  # Output: 3
print(solution([4, 7, 1, 5, 3]))  # Output: 4
print(solution([12, 12, 12, 15, 10]))  # Output: 3
print(solution([18, 26, 18, 24, 24, 20, 22]))  # Output: 5
