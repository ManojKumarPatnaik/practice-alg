def solution(N, A, B):
  """
  Checks whether there is a path from node 1 to node N in an undirected graph.

  Args:
    N (int): The number of nodes in the graph.
    A (list[int]): An array containing the source nodes of the edges.
    B (list[int]): An array containing the destination nodes of the edges.

  Returns:
    bool: True if there is a path from node 1 to node N, False otherwise.
  """

  # Create a dictionary to store the graph
  graph = {i: [] for i in range(1, N+1)}
  
  # Populate the graph with edges
  for i in range(len(A)):
    graph[A[i]].append(B[i])
    graph[B[i]].append(A[i])

  # Check if there is a path from 1 to N
  for i in range(1, N):
    if i + 1 not in graph[i]:
      return False

  return True

print(solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]))  # Output: True
print(solution(4, [1, 2, 1, 3], [2, 4, 3, 4]))  # Output: False
print(solution(6, [2, 4, 5, 3], [3, 5, 6, 4]))  # Output: False
print(solution(3, [1, 3], [2, 2]))  # Output: True