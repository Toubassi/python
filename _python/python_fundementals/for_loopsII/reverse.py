def reverese(nums):
  right = len(nums)-1
  left = 0
  while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp
    left += 1
    right -= 1
  return nums
print(reverese([1, 2, 3, 8]))