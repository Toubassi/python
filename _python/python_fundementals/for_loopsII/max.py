nums = []
def maximum(nums):
  if len(nums) == 0:
    return False
  maxi = nums[0]
  for i in range(len(nums)):
    if (nums[i] > maxi):
      maxi = nums[i]
  return maxi
print(maximum(nums))