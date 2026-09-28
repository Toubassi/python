nums = [-1,8,-3,9]

def minimum(nums):
  if len(nums) == 0:
    return False
  mini = nums[0]
  for i in range(len(nums)):
    if (nums[i] < mini):
      mini = nums[i]
  return mini
print(minimum(nums))