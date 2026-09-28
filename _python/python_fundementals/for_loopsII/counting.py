nums = [1, 8, 9]
def counting(nums):
  total = 0
  for i in range(len(nums)):
    total += i
  return total
print(len(nums))