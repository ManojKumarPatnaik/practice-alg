def solution(S):
  """Returns the length of the longest substring in which every letter occurs an even number of times.

  Args:
    S: A string consisting of N lowercase English letters.

  Returns:
    The length of the longest substring in which every letter occurs an even number of times.
    If no such substring exists, returns 0.
  """

  # Get the length of the string.
  N = len(S)

  # Initialize the longest substring length.
  longestEvenCount = 0

  # Iterate over the string, starting at index i.
  for i in range(N - 1):

    # Create a hash table to store the frequency of each letter in the substring.
    letterCount = {}

    # Iterate over the substring, starting at index j, which is i + 1.
    for j in range(i + 1, N, 2):

      # Increment the frequency of the current letter in the hash table.
      letterCount[S[j]] = letterCount.get(S[j], 0) + 1

      # Increment the frequency of the previous letter in the hash table.
      letterCount[S[j - 1]] = letterCount.get(S[j - 1], 0) + 1

      # If all the letters in the substring occur an even number of times, update the longest substring length.
      if letterCount[S[j]] % 2 == 0 and letterCount[S[j-1]] % 2 == 0:
        longestEvenCount = max(longestEvenCount, j - i + 1)

  # Return the longest substring length.
  return longestEvenCount

print(solution("bdaaadadb"))  # Output: 6
print(solution("abacb"))  # Output: 0
print(solution("zthtzh"))  # Output: 6