nums = [2,2,5,4,5]

def average(nums):
  total = 0
  for i in range(len(nums)):
    total += nums[i]
  avg = total / len(nums)
  return avg
print(average(nums))