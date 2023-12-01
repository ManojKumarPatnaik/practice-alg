def solution(S):
  """Returns any palindrome which can be obtained by replacing all of the question marks in S by lowercase letters ('a'-'z'). If no palindrome can be obtained, the function should return the string "NO".

  Args:
    S: A string of length N, consisting only of lowercase letters ('a'-'z') or '?'.

  Returns:
    A palindrome string, or the string "NO" if no palindrome can be obtained.
  """

  N = len(S)

  # Convert the string to a list.
  S = list(S)

  # Calculate the halfway point of the list.
  halfSize = N // 2

  # Loop through the first half of the list, replacing question marks with letters
  # from the second half.
  for i in range(halfSize):
    if S[i] == "?" and S[N - 1 - i] != "?":
      S[i] = S[N - 1 - i]
    elif S[N - 1 - i] == "?" and S[i] != "?":
      S[N - 1 - i] = S[i]
    elif S[i] == S[N - 1 - i] == "?":
      S[i] = S[N - 1 - i] = "a"
    else:
      # Return "NO" when first half and second half letters are different.
      return "NO"

  # If the loop completes without returning "NO", then the string is a palindrome.
  return ''.join(S)

print(solution("?ab??a"))  # Output: "aabbaa"
print(solution("bab??a"))  # Output: "NO"
print(solution("?a?"))  # Output: "aaa"
