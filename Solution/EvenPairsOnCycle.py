def solution(A):
  """Finds the maximum number of neighbouring pairs whose sums are even.

  Args:
    A: A list of integers.

  Returns:
    The maximum number of neighbouring pairs whose sums are even.
  """

  N = len(A)

  # Initialize a variable `count` to 0.
  count = 0

  # Create a set `paired` to keep track of which elements have already been paired.
  paired = set()

  # Iterate over the array A, starting from index 0.
  i = 0
  while i < N - 1:
    # Check if the sum of the current element and the next element is even.
    if (A[i] + A[i + 1]) % 2 == 0:
      # Add the current and next elements to the paired set.
      paired.add(i)
      paired.add(i + 1)
      # Increment the count variable.
      count += 1
      i += 2
    else:
      i += 1

  # Check if the last and first elements can be paired.
  # If the array has at least two elements, and the last and first elements have not
  # already been paired, and the sum of the last and first elements is even, then
  # the last and first elements can be paired.
  if len(A) > 1 and (0 and N - 1) not in paired and (A[0] + A[-1]) % 2 == 0:
    count += 1

  # Return the count variable.
  return count

print(solution([4, 2, 5, 8, 7, 3, 7]))  # Output: 2
print(solution([14, 21, 16, 35, 22]))  # Output: 1
print(solution([5, 5, 5, 5, 5, 5]))  # Output: 3
