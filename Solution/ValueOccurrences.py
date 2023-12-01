def solution(A):
  """
  Finds the minimum number of moves to achieve an array in which all values X that are present in the array occur exactly X times.

  Args:
    A: A sorted array of integers.

  Returns:
    The minimum number of moves.
  """

  # Create a dictionary to store the frequency of each element in the array.
  freq = {}
  for element in A:
    freq[element] = freq.get(element, 0) + 1

  # Count the number of moves required to make the frequency of each element equal to its value.
  moves = 0
  for element, count in freq.items():
    if count > element:
      # We can remove extra occurrences of the element.
      moves += count - element
    elif count < element:
      # We can insert new occurrences of the element. However, it is also possible to remove all occurrences of the element and insert a new occurrence. We need to choose the move that minimizes the number of moves.
      moves += min(element - count, count)

  return moves

# Examples
print(solution([1, 1, 3, 4, 4, 4]))  # Output: 3
print(solution([1, 2, 2, 2, 5, 5, 5, 8]))  # Output: 4
print(solution([1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4]))  # Output: 5
print(solution([10, 10, 10]))  # Output: 3
