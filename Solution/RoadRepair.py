def solution(S, B):
  """
  Finds the maximum number of potholes that can be fixed given a road
  described by a string S and a budget B.

  Args:
    S: A string representing the road, where each character represents a
      fragment of the road. '.' denotes a smooth surface and 'x' denotes a
      pothole.
    B: The budget for fixing potholes.

  Returns:
    The maximum number of potholes that can be fixed given the budget B.
  """

  # Split the road into segments of consecutive potholes
  segments = S.split('.')

  # Filter out empty segments and calculate the cost for each segment
  potholesCost = [(len(segment) + 1) for segment in segments if segment]

  fixedPotholes = 0
  for cost in sorted(potholesCost, reverse=True):
    if B >= cost:
      # If we have enough budget, fix this segment
      B -= cost
      fixedPotholes += cost - 1
    else:
      # If we don't have enough budget for the whole segment,
      # fix as many potholes as we can
      fixedPotholes += B - 1
      break

  return fixedPotholes

print(solution("...xxx..x....xxx.", 7))  # Output: 5
print(solution("..xxxxx", 4))  # Output: 3
print(solution("x.x.xxx...x", 14))  # Output: 6
print(solution("..", 5))  # Output: 0