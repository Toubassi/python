nums = [1,2,3,4,5]

def sum_total(nums):
  total = 0
  for i in range(len(nums)):
    total += nums[i]
  return total
print(sum_total(nums))