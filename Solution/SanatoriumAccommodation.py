def solution(A):
  """
  Find the minimum number of rooms needed to accommodate all guests.

  Args:
      A: A list of integers, where the K-th guest wants to be in a room
          that contains at most A[K] guests, including themselves.

  Returns:
      The minimum number of rooms needed to accommodate all guests.
  """

  # Sort the guests by their desired room capacity.
  sortedA = sorted(A)

  # Initialize the number of rooms.
  rooms = 0

  # Initialize the current room capacity.
  availAccomodations = 0

  # Iterate over the guests.
  for accommodate in sortedA:

    # If the current room capacity is zero, then we need to create a new room.
    if availAccomodations == 0:
      availAccomodations = accommodate
      rooms += 1

    # Update the current room capacity.
    availAccomodations -= 1

  # Return the number of rooms needed.
  return rooms

print(solution([1, 1, 1, 1, 1]))  # Output: 5
print(solution([2, 1, 4]))  # Output: 2
print(solution([2, 7, 2, 9, 8]))  # Output: 2
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))  # Output: 4