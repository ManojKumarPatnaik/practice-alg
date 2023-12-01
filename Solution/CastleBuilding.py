def solution(A):
  """
  Counts the number of castles that can be built on the border with Servia.

  Args:
    A: A list of integers representing the height of the terrain at each segment of
      the border.

  Returns:
    The total number of castles that can be built on the border.
  """

  borderLen = len(A)

  # Checks if the input array is empty. If it is, the function returns 0.
  if (borderLen == 0):
    return 0
  
  # Initializes the counter for the number of castles.
  castles = 0
  # Stores the value of the first element of the array in the variable `prevValue`.
  prevValue = A[0]

  for i in range(1, borderLen - 1):
    # Checks if the current element is different from the previous element and the next element.
    # If it is, then the current element is either the beginning or end of a hill or valley,
    # and the counter is incremented.
    if(((A[i] - prevValue) * (A[i + 1] - A[i])) < 0):
      castles += 1
      prevValue = A[i]

  # Checks if the counter is equal to 0.
  # If it is, then there are no hills or valleys in the array.
  # The if statement then checks if the first element of the array is equal to the last element of the array.
  # If it is, then there is a single hill or valley, and the function returns 1.
  if(castles == 0):
    if(A[0] == A[borderLen - 1]):
      return 1
  # Count the two castles that can be built at the edges of the array,
  # even if there are no hills or valleys in the array.
  return castles + 2

print(solution([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]))  # Output: 4
print(solution([-3, -3]))  # Output: 1
