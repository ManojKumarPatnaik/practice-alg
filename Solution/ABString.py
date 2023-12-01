def solution(S):
  """Returns True if all occurrences of 'a' are before all occurrences of 'b' in the string S, False otherwise.

  Args:
    S: A string consisting of only the characters 'a' and 'b'.

  Returns:
    A boolean value indicating whether all occurrences of 'a' are before all occurrences of 'b' in the string S.
  """

  # Iterate over the string.
  # If the current character is 'b' and the next character is 'a', then return False.
  if "ba" in S:
      return False

  # If we reach here, then all 'a's must be before all 'b's, so return True.
  return True
    
print(solution("aabbb"))  # Output: True
print(solution("ba"))  # Output: False
print(solution("aaa"))  # Output: True
print(solution("b"))  # Output: True
print(solution("abba"))  # Output: False