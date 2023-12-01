def solution(S):
  """
  Splits a string into a minimal number of substrings in such a way that no letter occurs more than once in each substring.

  Args:
    S: A string consisting of lowercase letters of the English alphabet.

  Returns:
    The minimum number of substrings into which the string has to be split.
  """

  # Initialize a dictionary to store the last seen index of each character
  lastSeenChar = {}

  # Initialize a variable to keep track of the start of the current substring
  subStringStartPoint = 0

  # Initialize a variable to count the number of substrings
  numberSubStrings = 0

  # Iterate over the string
  for i in range(len(S)):
    # If the current character has been seen before and its last seen index is within the current substring
    if S[i] in lastSeenChar and lastSeenChar[S[i]] >= subStringStartPoint:
      # Start a new substring from the current index
      subStringStartPoint = i

      # Increment the count of substrings
      numberSubStrings += 1

    # Update the last seen index of the current character
    lastSeenChar[S[i]] = i
    
  # Return the total number of substrings, accounting for the last substring
  return numberSubStrings + 1

print(solution("abacdec"))  # Output: 3
print(solution("world"))  # Output: 1
print(solution("dddd"))  # Output: 4
print(solution("cycle"))  # Output: 2
print(solution("abba"))  # Output: 2