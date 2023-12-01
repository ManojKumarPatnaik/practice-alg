def solution(N):
  """Generates a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.
  
  Args:
    N: An integer within the range [1..200,000].

  Returns:
    A string of length N containing as many different lower-case letters as possible, in which each letter occurs an equal number of times.
  """

  # Calculate the frequency of each letter.
  freq = 1
  blockSize = 26
  if N > 26:
    while blockSize > 1:
      if (N % blockSize == 0):
        break
      blockSize -= 1
    freq = N // blockSize

  # If N less than 26, each letter occurs one time in string of length N.
  else:
    blockSize = N

  lowerLetters = "abcdefghijklmnopqrstuvwxyz"
  return lowerLetters[0:blockSize] * freq

print(solution(3))  # Output: "abc"
print(solution(5))  # Output: "abcde"
print(solution(30))  # Output: "aabbcc...oo"
