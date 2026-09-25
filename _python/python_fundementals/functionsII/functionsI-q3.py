numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def first_plus_length(numbers):
  first_value = numbers[0]
  list_length = len(numbers)
  return first_value + list_length
print(first_plus_length(numbers))