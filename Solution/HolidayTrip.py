def solution(P, S):
  """
  Finds the minimum number of cars needed to take all friends on holiday.

  Args:
    P: A list of integers, where P[K] is the number of people in the K-th car.
    S: A list of integers, where S[K] is the number of seats in the K-th car.

  Returns:
    An integer, the minimum number of cars needed to take all friends on holiday.
  """

  # Calculate the total number of people.
  totalPeople = sum(P)
  # Initialize the minimum number of cars needed.
  minCars = 0
  # Sorted seats, in decreasing order.
  S.sort(reverse=True)
  # Iterate over the sorted list of seats.
  for seat in S:
    # Add the current seat to the available seats.
    totalPeople -= seat
    # Increment the minimum number of cars needed.
    minCars += 1
    # If the number of available seats is greater than or equal to the total
    # number of people, then we have found the minimum number of cars needed.
    if totalPeople <= 0:
      break
  # Return the minimum number of cars needed.
  return minCars

print(solution([1, 4, 1], [1, 5, 1]))  # Output: 2
print(solution([4, 4, 2, 4], [5, 5, 2, 5]))  # Output: 3
print(solution([2, 3, 4, 2], [2, 5, 7, 2]))  # Output: 2
