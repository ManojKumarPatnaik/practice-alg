def solution(A):
  """
  Finds the length of the longest consistent fragment of A in which all elements can be generated using at most two different digits.
  You must use the same digits for all elements.

  Args:
    A: A list of integers.

  Returns:
    The length of the longest consistent fragment of A in which all elements can have different digits.
  """

  # Determine the length of the input array
  N = len(A)

  # Initialize the maximum fragment length to 0
  longest_fragment = 0

  # Iterate through the array starting from the second element
  for i in range(N - 1):
    # Create a set to store the unique digits of the current element
    digits = set(str(A[i]))

    # Check if the current element has more than two distinct digits
    if len(digits) > 2:
      # If so, skip to the next iteration
      continue

    # Initialize the current fragment length to 1
    current_fragment = 1

    # Iterate through the remaining elements
    for j in range(i + 1, N):
      # Update the set of unique digits with the digits of the current element
      digits.update(set(str(A[j])))

      # Check if the updated set has more than two distinct digits
      if len(digits) > 2:
        # If so, break out of the loop
        break

      # Increment the current fragment length
      current_fragment += 1

    # Update the maximum fragment length if the current fragment is longer
    longest_fragment = max(longest_fragment, current_fragment)

  # Return the maximum fragment length
  return longest_fragment

print(solution([23, 333, 33, 30, 0, 505]))  # Output: 4
print(solution([615, 88, 498, 99, 9]))  # Output: 2
print(solution([123, 456]))  # Output: 0
