def solution(S):
  """Returns the alphabetically smallest string that can be obtained by removing exactly one letter from S.

  Args:
    S: A string consisting of N characters, where N is an integer within the range [2..100,000] and string S is made only of lowercase letters (a-z).

  Returns:
    A string representing the alphabetically smallest string that can be obtained by removing exactly one letter from S.
  """

  # Iterate over the string, starting at the second character.
  for i in range(len(S) - 1):
    # If the current character is greater than the next character, then remove the current character and update the smallest string.
    if S[i] > S[i + 1]:
      return S[:i] + S[i + 1:]

  # If we reach the end of the string without finding any such character, then remove the last character from the string.
  return S[:-1]

print(solution("acb"))  # Output: ab
print(solution("hot"))  # Output: ho
print(solution("codility"))  # Output: cdility
print(solution("aaaa"))  # Output: aaa
