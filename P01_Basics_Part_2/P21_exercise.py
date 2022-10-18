def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8]))


def lowest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return min(evens)

print(lowest_even([10,1,2,3,4,8]))