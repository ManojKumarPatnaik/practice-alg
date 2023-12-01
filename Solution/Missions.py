def solution(D, X):
  """
  Returns the minimum number of days required to complete all of the missions in the game without sorting the array D.

  Args:
    D: A list of integers representing the difficulty levels of the missions.
    X: The maximum difference in difficulty between any two missions that can be completed on the same day.

  Returns:
    An integer representing the minimum number of days required to complete all of the missions.
  """

  # Initialize the current day,
  # and the list contains min, max difficulty missions that can be completed on the current day.
  days = 1
  sameDayMissions = [D[0], D[0]]
  # Iterate through the missions.
  for i in range(1, len(D)):
    # If the difference in difficulty between the current mission and either of the missions that can be completed on the current day is greater than X,
    # then the current mission cannot be completed on the current day.
    if abs(D[i] - sameDayMissions[0]) > X or abs(D[i] - sameDayMissions[1]) > X:
      # Increment the current day and reset the min, max difficulty missions that can be completed on the current day.
      days += 1
      sameDayMissions = [D[i], D[i]]
    else:
      # Otherwise, update the list contains min, max difficulty missions with the current mission.
      sameDayMissions = [min(sameDayMissions[0], D[i]), max(sameDayMissions[1], D[i])]
  # Return the current day.
  return days

print(solution([5, 8, 2, 7], 3)) # Output: 3
print(solution([2, 5, 9, 2, 1, 4], 4)) # Output: 3
print(solution([1, 12, 10, 4, 5, 2], 2)) # Output: 4