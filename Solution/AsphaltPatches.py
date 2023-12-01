def solution(S):
  """
  Computes the minimum number of patches required to repair all the potholes in the road.

  Args:
    S: A string of length N, where each character is either '.' or 'X'.

  Returns:
    An integer representing the minimum number of patches required to repair all the
    potholes in the road.
  """

  # Initialize the number of patches.
  patches = 0

  # Iterate over the string with step 3.
  for i in range(0, len(S), 3):
    # Patch the road if there is at least one pothole in the current segment.
    if 'X' in S[i:i + 3]:
      patches += 1

  # Return the number of patches.
  return patches

print(solution(".X..X"))  # Output: 2
print(solution("X.XXXXX.X."))  # Output: 3
print(solution("XX.XXX.."))  # Output: 2
print(solution("XXXX"))  # Output: 2
