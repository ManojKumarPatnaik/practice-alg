def solution(A):
  """Finds the number of doctors working at more than one hospital.

  Args:
    A: A two-dimensional array representing the hospitals' schedules.

  Returns:
    The number of doctors working at more than one hospital.
  """

  hospitals = len(A)
  days = len(A[0])
  doctors = {}

  # Create a set to store the hospitals that each doctor works at.
  for i in range(hospitals):
    for j in range(days):
      if A[i][j] not in doctors:
        doctors[A[i][j]] = set()
      doctors[A[i][j]].add(i)

  moreThanAHospitals = 0

  # Iterate through the dictionary of doctors and their hospitals.
  for doctor, hospitals in doctors.items():

    # If the doctor works at more than one hospital, increment the counter.
    if len(hospitals) > 1:
      moreThanAHospitals += 1

  return moreThanAHospitals

print(solution([[1, 2, 2], [3, 1, 4]]))  # Output: 1
print(solution([[1, 1, 5, 2, 3], [4, 5, 6, 4, 3], [9, 4, 4, 1, 5]]))  # Output: 4
print(solution([[4, 3], [5, 5], [6, 2]]))  # Output: 0