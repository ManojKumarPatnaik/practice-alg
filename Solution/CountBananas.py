def solution(S):
  """
  Finds the maximum number of times the word "BANANA" can be deleted from a string.

  Args:
    S: A string of uppercase English letters.

  Returns:
    The maximum number of times the word "BANANA" can be deleted from S.
  """

  # Count the occurrences of B, A and N letters in S.
  counts = {"B": 0, "A": 0, "N": 0}
  for letter in S:
    if letter in ["B", "A", "N"]:
        counts[letter] += 1

  # Calculate the minimum number of times "BANANA" can be deleted from S.
  maxBananas = min(
      counts.get("B", 0) // 1,
      counts.get("A", 0) // 3,
      counts.get("N", 0) // 2,
  )

  return maxBananas
  
print(solution("NAABXXAN"))  # Output: 1
print(solution("NAANAAXNABABYNNBZ"))  # Output: 2
print(solution("QABAAAWOBL"))  # Output: 0
