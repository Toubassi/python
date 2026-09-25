def values_greater_than_second(numbers):
  if len(numbers) < 2:
    return False
  second_value = numbers[1]
  new = []
  for x in numbers:
    if x > second_value:
      new.append(x)
  print(len(new))
  return new
  print(new)

print(values_greater_than_second([5, 1, 6, 7, 8, 2]))
print(values_greater_than_second([5]))
