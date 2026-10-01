nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
def even_num(nums):
  for x in range(len(nums) - 1, -1, -1):
    if (nums[x] % 2 != 0):
      nums.pop(x)
  return nums

print(even_num(nums))