def findMaxPotholes(L1, L2):
  N = len(L1)
  repairSegmentsL1 = [0] * N  # Number of potholes that can be repaired in L1
  repairSegmentsL2 = [0] * N  # Number of potholes that can be repaired in L2
    
  # Calculate the number of potholes that can be repaired in L1 from each segment to the end
  for i in range(N - 2, -1, -1):
    repairSegmentsL1[i] = repairSegmentsL1[i + 1]
    if L1[i + 1] == "x":
      repairSegmentsL1[i] += 1

  # Calculate the number of potholes that can be repaired in L2 from the start to each segment
  for i in range(1, N):
    repairSegmentsL2[i] = repairSegmentsL2[i - 1]
    if L2[i - 1] == "x":
      repairSegmentsL2[i] += 1

  # Return the maximum number of potholes that can be repaired
  return max([repairSegmentsL1[i] + repairSegmentsL2[i] for i in range(N)])

def solution(L1, L2):
  """
  Calculates the maximum number of segments with potholes that can be repaired.

  Args:
    L1: A string representing the first lane, where '.' denotes a smooth segment of road and 'x' denotes a segment containing potholes.
    L2: A string representing the second lane, where '.' denotes a smooth segment of road and 'x' denotes a segment containing potholes.

  Returns:
    The maximum number of segments with potholes that can be repaired.
  """

  # If one lane is full of potholes, repair that lane
  if L1.count('x') == len(L1):
    return L1.count('x')
  if L2.count('x') == len(L2):
    return L2.count('x')

  # If one lane is smooth, repair the other lane
  if L1.count('.') == len(L1):
    return L2.count('x')
  if L2.count('.') == len(L2):
    return L1.count('x')

  # Return the maximum number of potholes that can be repaired starting from either lane
  return max(findMaxPotholes(L1, L2), findMaxPotholes(L2, L1))

print(solution("..xx.x.", "x.x.x.."))  # Output: 4
print(solution(".xxx...x", "..x.xxxx"))  # Output: 6
print(solution("xxxxx", ".x..x"))  # Output: 5
print(solution("x...x", "..x.."))  # Output: 2