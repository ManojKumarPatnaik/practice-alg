def solution(S):
  """Finds the length of the shortest unique substring of a string S.

  Args:
    S: A string of lowercase letters.

  Returns:
    The length of the shortest unique substring of S, or 0 if no such substring
    exists.
  """

  # S is a minimum substring in the worst case.
  min_substrings = len(S)

  # Iterate over the string S and check if each substring is unique.
  for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):

      # Check if the substring is unique by checking if its first occurrence is
      # also its last occurrence.
      if S.find(S[i:j]) == S.rfind(S[i:j]):
        min_substrings = min(min_substrings, len(S[i:j]))

  return min_substrings

print(solution("abaaba"))  # Output: 2
print(solution("zyzyzyz"))  # Output: 5
print(solution("aabbbabaaa"))  # Output: 3