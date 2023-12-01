def solution(S):
  """Returns the minimum number of moves required to obtain a string containing no instances of three identical consecutive letters.

  Args:
    S: A string consisting only of the characters 'a' and 'b'.

  Returns:
    An integer representing the minimum number of moves required.
  """

  N = len(S)
  # Check if the string is too short to have three identical consecutive letters.
  if N < 3:
    return 0

  newS = list(S)
  # Create a copy of the string to mutate.
  moves = 0
  # Initialize the number of moves required.
  trioBlock = 1
  # Initialize the counter for the number of identical consecutive letters.
  for i in range(1, N):
    # Iterate over the string starting from the second character.
    if newS[i] != newS[i - 1]:
      # If the current character is different from the previous character, reset the counter.
      trioBlock = 1
    else:
      # Otherwise, increment the counter.
      trioBlock += 1

    if trioBlock == 3:
      # If we have three identical consecutive letters, we need to make a move.
      if i == N - 1:
        # If the current character is the last character in the string, we need to swap it.
        moves += 1
      else:
        # Otherwise, we can swap either the current character or the previous character.
        if newS[i] == newS[i + 1]:
          # If the current character is the same as the next character, swap it.
          newS[i] = "b" if newS[i] == "a" else "a"
        else:
          # Otherwise, swap the previous character.
          newS[i - 1] == "b" if newS[i] == "a" else "a"
        moves += 1
      trioBlock = 1

  return moves

print(solution("baaaaa"))  # Output: 1
print(solution("baaabbaabbba"))  # Output: 2
print(solution("baabab"))  # Output: 0
