def solution(S):
  """
  Finds the minimum number of water tanks needed to collect rainwater from all of the houses on a street.

  Args:
    S: A string describing the street, where 'H' denotes a house and '−' denotes an empty plot.

  Returns:
    The minimum number of water tanks needed, or -1 if there is no solution.
  """

  # If there is only one house, then there is no solution.
  if len(S) == 1:
    return -1

  # Initialize the number of water tanks and the last tank position.
  tanks = 0
  lastTankPosition = -1

  # Iterate over the houses on the street.
  for i in range(len(S)):

    # Check if the house is next to an empty plot on the left or right.
    isLeftEmptyPlot = False
    isRightEmptyPlot = False
    if S[i] == "H":
      if i != 0 and S[i - 1] == "-":
        isLeftEmptyPlot = True
      if i != len(S) - 1 and S[i + 1] == "-":
        isRightEmptyPlot = True

      # If the house is not next to an empty plot on either side, then there is no solution.
      if not isLeftEmptyPlot and not isRightEmptyPlot:
        return -1

      # If the house is next to an empty plot on the right and there is no tank on the left,
      # then place a tank on the right.
      if isRightEmptyPlot and (lastTankPosition != i - 1 or not isLeftEmptyPlot):
        tanks += 1
        lastTankPosition = i + 1

      # If the house is next to an empty plot on the left and there is no tank on the right,
      # then place a tank on the left.
      if isLeftEmptyPlot and not isRightEmptyPlot and lastTankPosition != i - 1:
        tanks += 1
        lastTankPosition = i - 1

  # Return the number of water tanks needed.
  return tanks

print(solution("-H-HH--"))  # Output: 2
print(solution("H"))  # Output: -1
print(solution("HH-HH"))  # Output: -1
print(solution("-H-H-H-H-H"))  # Output: 3
