def solution(S):
  """
  Finds a pair of strings in array S that share a common letter at some index, or returns an empty array if no such pair exists.

  Args:
    S: A list of strings of the same length.

  Returns:
    An array containing three integers, representing the indexes in S of the strings belonging to the pair and the position of the common letter, or an empty array if no such pair exists.
  """

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  # Creates a lookup table with 26 buckets, one for each letter in the alphabet.
  # Each bucket is a dictionary that maps letters to their corresponding positions in the strings in S.
  lookup = [{letter: None for letter in alphabet} for i in range(len(S[0]))]

  # Iterates over the strings in S and updates the lookup table.
  for stringPos in range(len(S)):
    for letterPos in range(len(S[0])):
      currentLetterPos = lookup[letterPos][S[stringPos][letterPos]]

      # If the letter is not in the lookup table, adds it to the lookup table.
      if currentLetterPos is None:
        lookup[letterPos][S[stringPos][letterPos]] = stringPos
      else:
        # If the letter is already in the lookup table, returns an array containing the indexes of the strings and the position of the common letter.
        return [min(currentLetterPos, stringPos), max(currentLetterPos, stringPos), letterPos]

  # Returns an empty array if no such pair exists.
  return []

print(solution(["abc", "bca", "dbe"]))  # Output: [0, 2, 1]
print(solution(["zzzz", "ferz", "zdsr", "fgtd"]))  # Output: [0, 1, 3]
print(solution(["gr", "sd", "rg"]))  # Output: []
print(solution(["bdafg", "ceagi"]))  # Output: [0, 1, 2]