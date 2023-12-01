def solution(A):
  """
  Finds the minimum number of actions needed to make all sections of a garden contain the same number of trees.

  Args:
    A: A list of integers, where A[K] denotes the number of trees in the K-th section of the garden.

  Returns:
    The minimum number of actions needed to make all sections of the garden contain the same number of trees.
  """

  # Get number of the sections
  N = len(A)

  # Calculate the total number of trees in the garden.
  total = sum(A)

  # Calculate the desired number of trees per section.
  desiredTrees = total // N

  # Check if the total number of trees is divisible by the number of sections.
  # If it is not, we need to plant a tree in each section with a deficit.
  if total % N == 0:
    desiredTrees = total // N
  else:
    desiredTrees = (total + (N - (total % N))) // N

  # Initialize the number of actions required.
  actions = 0

  # Iterate over the trees in the garden and count the number of trees in excess or in deficit in each section.
  for tree in A:
    # If the tree has more trees than desired, we need to replant some trees to other sections.
    if tree < desiredTrees:
      actions += desiredTrees - tree

  return actions

print(solution([1, 2, 2, 4]))  # Output: 4
print(solution([4, 2, 4, 6]))  # Output: 2
print(solution([1, 1, 2, 1]))  # Output: 3
