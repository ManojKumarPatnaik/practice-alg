def solution(A, R):
  """Returns the maximum number of types of items that can be stored in the storeroom after freeing R consecutive shelves.

  Args:
    A: A list of integers representing the types of items stored on storeroom shelves.
    R: The number of consecutive shelves to be freed.

  Returns:
    The maximum number of types of items that can still be stored in the storeroom after freeing R consecutive shelves.
  """

  # Get the length of the input array.
  N = len(A)

  # Initialize the maximum number of types of items that can still be stored in the storeroom.
  maxTypes = 0

  # Iterate over the possible start indices of the R consecutive shelves to be freed.
  for i in range(N - R + 1):
    # Create a list of the items that will remain in the storeroom after freeing the R consecutive shelves.
    afterFreeing = A[:i] + A[i + R:] if i > 0 else A[i + R:]

    # Calculate the number of different types of items in the list.
    currentTypes = len(set(afterFreeing))

    # Update the maximum number of types of items that can still be stored in the storeroom.
    maxTypes = max(maxTypes, currentTypes)

  return maxTypes

print(solution([2, 1, 2, 3, 2, 2], 3))  # Output: 2
print(solution([2, 3, 1, 1, 2], 2))  # Output: 3
print(solution([20, 10, 10, 10, 30, 20], 3))  # Output: 3
print(solution([1, 100000, 1], 3))  # Output: 0
