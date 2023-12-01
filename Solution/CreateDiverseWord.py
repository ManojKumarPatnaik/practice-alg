def solution(AA, AB, BB):
  """Returns the longest string that can be created without containing AAA or BBB,
  given the number of times AA, AB, and BB appear.

  Args:
    AA: The number of times AA appears.
    AB: The number of times AB appears.
    BB: The number of times BB appears.

  Returns:
    A string that is the longest possible without containing AAA or BBB.
  """

  # Initialize the longest string.
  longestString = ""

  # Add the first string to the longest string.
  if BB > 0:
    longestString += "BB"
    BB -= 1
  elif AB > 0:
    longestString += "AB"
    AB -= 1
  else:
    longestString += "AA"
    AA -= 1

  # Add an AB string to the longest string if possible and necessary.
  while AB > 0:
    if longestString[-1] != "A":
      longestString += "AB"
    elif longestString[0] != "B":
      longestString = "AB" + longestString
    AB -= 1

  # Initialize the current length of the longest string.
  currentLength = len(longestString)

  # While there are still strings available, add them to the longest string.
  while AA > 0 or BB > 0:
    # Add a BB string to the longest string if possible and necessary.
    if BB > 0 and longestString[-1] != "B":
      longestString += "BB"
      BB -= 1
    # Add a BB string to the beginning of the longest string if possible and necessary.
    if BB > 0 and longestString[0] != "B":
      longestString = "BB" + longestString
      BB -= 1
    # Add an AA string to the longest string if possible and necessary.
    if AA > 0 and longestString[-1] != "A":
      longestString += "AA"
      AA -= 1
    # Add an AA string to the beginning of the longest string if possible and necessary.
    if AA > 0 and longestString[0] != "A":
      longestString = "AA" + longestString
      AA -= 1

    # Update the current length of the longest string.
    if currentLength < len(longestString):
      currentLength = len(longestString)
    else:
      # If the current length of the longest string has not changed, then the longest string has been found.
      break

  # Return the longest string.
  return longestString

print(solution(5, 0, 2))  # Output: AABBAABBAA
print(solution(1, 2, 1))  # Output: BBABABAA
print(solution(0, 2, 0))  # Output: ABAB
print(solution(0, 0, 10))  # Output: BB