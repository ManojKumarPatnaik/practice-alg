def solution(S):
  """Finds the number of splits S satisfying the condition.

  Args:
      S: A string consisting of N lowercase English letters.

  Returns:
      The number of splits S satisfying the condition.
  """

  # Initializes two lists, countX and countY,
  # to store the prefix sums of the occurrences of x and y in the string S, respectively.
  countX = [0] * (len(S) + 1)
  countY = [0] * (len(S) + 1)

  # Calculate prefix sums
  for i in range(len(S)):
    countX[i+1] = countX[i] + 1 if S[i] == 'x' else countX[i]
    countY[i+1] = countY[i] + 1 if S[i] == 'y' else countY[i]

  numberEqualSplits = 0
  for i in range(1, len(S)):
    if (countX[i] == countY[i]) or (countX[len(S)] - countX[i] == countY[len(S)] - countY[i]):
      numberEqualSplits += 1

  return numberEqualSplits

print(solution("ayxbx"))  # Output: 3
print(solution("xzzzy"))  # Output: 0
print(solution("toyxmy"))  # Output: 5
print(solution("apple"))  # Output: 4