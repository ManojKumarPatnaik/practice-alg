def solution(S):
  """
  Counts the number of times the first letter of a string is the same as the last letter
  after performing N-1 operations of moving the first letter to the end.

  Args:
    S: A string of length N, consisting of letters 'a' and/or 'b'.

  Returns:
    An integer representing the number of times the first letter is the same as the
    last in the obtained sequence of strings.
  """

  # Perform N-1 operations of moving the first letter to the end.
  for i in range(len(S)):
    # Count the number of times the first letter is the same as the last in the current string.
    if S[0] == S[-1]:
      count += 1

    S = S[1:] + S[0]

  return count

print(solution("abbaa"))  # Output: 3
print(solution("aaaa"))  # Output: 4
print(solution("abab"))  # Output: 0
