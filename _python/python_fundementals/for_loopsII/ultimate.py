# nums = [-1,8,-3,9]

def ultimate(nums):
  maxi = nums[0]
  mini = nums[0]
  length = len(nums)
  total = 0
  x= 1
  
  # if len(nums) == 0:
  #   return False

  for i in range(len(nums)):
    total += nums[i]
    
    if (nums[i] < mini):
      mini = nums[i]
    if (nums[i] > maxi):
      maxi = nums[i]
  avg = total / length
  print(f"sumTotal: {total}, average: {avg}, minimum: {mini}, maximum: {maxi}, length: {length}")
ultimate([-1,8,-3,9])
