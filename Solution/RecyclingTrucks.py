def solution(D, T):
  """
  Finds the minimum number of minutes needed by the trucks to finish all the jobs.

  Args:
    D: A list of integers representing the time it takes to travel between
      houses.
    T: A list of strings representing the types of trash collected at each house.

  Returns:
    An integer representing the minimum number of minutes needed by the trucks
      to finish all the jobs.
  """

  # Initialize count lists for each type of trash
  plasticCount = [0] * len(T)
  glassCount = [0] * len(T)
  metalCount = [0] * len(T)

  # Initialize variables to keep track of the last house that has each type of trash
  plasticLastHouse = 0
  glassLastHouse = 0
  metalLastHouse = 0

  # Iterate over each house
  for i in range(len(T)):
    # Count the number of plastic bags in the current house and update plasticLastHouse if necessary
    plasticCount[i] = T[i].count("P")
    if plasticCount[i] > 0:
      plasticLastHouse = i

    # Count the number of glass bags in the current house and update glassLastHouse if necessary
    glassCount[i] = T[i].count("G")
    if glassCount[i] > 0:
      glassLastHouse = i  

    # Count the number of metal bags in the current house and update metalLastHouse if necessary
    metalCount[i] = T[i].count("M")
    if metalCount[i] > 0:
      metalLastHouse = i

  # Calculate the total time for the truck collecting plastic to finish its job and return to the starting point
  plasticCollectTime = sum(D[:plasticLastHouse + 1]) * 2 + sum(plasticCount)
  
  # Calculate the total time for the truck collecting glass to finish its job and return to the starting point
  glassCollectTime = sum(D[:glassLastHouse + 1]) * 2 + sum(glassCount)
    
  # Calculate the total time for the truck collecting metal to finish its job and return to the starting point
  metalCollectTime = sum(D[:metalLastHouse + 1]) * 2 + sum(metalCount)

  # Return the maximum of these times, which represents the minimum time for all trucks to finish their jobs
  return (max(plasticCollectTime, glassCollectTime, metalCollectTime))

print(solution([2, 5], ["PGP", "M"]))  # Output: 15
print(solution([3, 2, 4], ["MPM", "", "G"]))  # Output: 19
print(solution([2, 1, 1, 1, 2], ["", "PP", "PP", "GM", ""]))  # Output: 12
