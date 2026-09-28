
def count_positives(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] > 0:
      count +=1
    else:
      continue
  nums[-1] = count
  return nums
  
print(count_positives())
