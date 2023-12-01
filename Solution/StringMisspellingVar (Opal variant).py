def solution(S, T):
  """
  Determines whether string T can be obtained from string S by at most one simple operation from a specified set.
  :param S: The original string
  :param T: The target string
  :return: A string indicating the operation performed or "IMPOSSIBLE" if no operation is possible
  """

  # Check if S and T are equal
  if S == T:
    return "EQUAL"  # Strings are equal

  # Handle inserting a character at the beginning of S
  if T[1:] == S:
    return f"INSERT {T[0]}"  # Insert the first character of T if T[1:] equals S

  # Handle removing a character from the end of S
  if S[:len(S)-1] == T:
    return f"REMOVE {S[len(S)-1]}"  # Remove the last character of S if S[:len(S)-1] equals T

  # Handle swapping adjacent characters in S
  countS = sorted({letter: S.count(letter) for letter in S}.items())
  countT = sorted({letter: T.count(letter) for letter in T}.items())
  if countS == countT:  # Check if character counts are equal
    swaps = []
    for i in range(1, len(S)):  # Iterate through characters in S
      if S[i] != T[i] and S[i] == T[i - 1] and S[i - 1] == T[i]:
        swaps.append((S[i - 1], S[i]))  # Add swap pairs to the list

    if len(swaps) == 1:  # Handle a single swap
      return f"SWAP {swaps[0][0]} {swaps[0][1]}"  # Return the swap operation

  # If no operation applies, return "IMPOSSIBLE"
  return "IMPOSSIBLE"

print(solution("gain", "again"))  # Output: INSERT a
print(solution("parks", "park"))  # Output: REMOVE s
print(solution("form", "from"))  # Output: SWAP o r
print(solution("o", "odd"))  # Output: IMPOSSIBLE
print(solution("fift", "fifth"))  # Output: IMPOSSIBLE